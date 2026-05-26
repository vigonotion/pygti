import base64
import hashlib
import hmac
import json

from aiohttp import ClientConnectorError, ClientResponse, ClientSession

from .exceptions import *

GTI_DEFAULT_HOST = "gti.geofox.de"


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
        self, method: str, path: str, payload=None, language: str = 'de', version: int = 1, **kwargs
    ) -> ClientResponse:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        payload_dict = json.loads(payload.model_dump_json(warnings=False))
        payload_dict['language'] = language
        payload_dict['version'] = version
        data = json.dumps(payload_dict).encode("UTF-8")

        signature = base64.b64encode(
            hmac.new(self.password.encode("UTF-8"), data, hashlib.sha1).digest()
        ).decode("UTF-8")

        headers["geofox-auth-signature"] = f"{signature}"
        headers["geofox-auth-user"] = self.username

        headers["Content-Type"] = "application/json"

        try:
            response = await self.websession.request(
                method,
                f"https://{self.host}{path}",
                data=data,
                **kwargs,
                headers=headers,
            )

            response_data = await response.json()

            return_code = response_data.get("returnCode")
            error_text = response_data.get("errorText")
            error_dev_info = response_data.get("errorDevInfo")

            if return_code == "ERROR_CN_TOO_MANY":
                raise CheckNameTooMany(return_code, error_text, error_dev_info)
            elif return_code == "ERROR_COMM":
                raise CommunicationError(return_code, error_text, error_dev_info)
            elif return_code == "ERROR_ROUTE":
                raise RouteError(return_code, error_text, error_dev_info)
            elif return_code == "ERROR_TEXT":
                if error_dev_info == "Authentication failed!":
                    raise InvalidAuth(return_code, error_text, error_dev_info)
                raise GTIError(return_code, error_text, error_dev_info)

            return response_data
        except ClientConnectorError as error:
            raise CannotConnect(error)
