import base64
import hashlib
import hmac
import json

from aiohttp import ClientResponse, ClientSession

GTI_DEFAULT_HOST = "api-test.geofox.de"


class Auth:
    """Class to make authenticated requests to the geofox api."""

    def __init__(
        self,
        websession: ClientSession,
        username: str,
        password: str,
        host: str = GTI_DEFAULT_HOST,
    ):
        """Initialize the auth."""
        self.websession = websession
        self.username = username
        self.password = password
        self.host = host

    async def request(
        self, method: str, path: str, payload=None, **kwargs
    ) -> ClientResponse:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        payload.update({"version": 37})

        data = json.dumps(payload).encode("UTF-8")

        signature = base64.b64encode(
            hmac.new(self.password.encode("UTF-8"), data, hashlib.sha1).digest()
        ).decode("UTF-8")

        print(payload)
        print(signature)

        headers["geofox-auth-signature"] = f"{signature}"
        headers["geofox-auth-user"] = self.username

        return await self.websession.request(
            method,
            f"http://{self.host}/{path}",
            json=payload,
            **kwargs,
            headers=headers,
        )
