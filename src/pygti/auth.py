import base64
import hashlib
import hmac
import json
from typing import Any

from aiohttp import ClientSession
from pydantic import BaseModel

from .exceptions import GTIError
from .models import ReturnCode

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
        self,
        method: str,
        path: str,
        payload: BaseModel,
        language: str = "de",
        version: int = 1,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Make a request."""
        headers = kwargs.pop("headers", None)

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        payload_dict: dict[str, Any] = payload.model_dump(
            mode="json", exclude_none=True, warnings=False
        )
        payload_dict["language"] = language
        payload_dict["version"] = version
        data = json.dumps(payload_dict).encode("UTF-8")

        signature = base64.b64encode(
            hmac.new(self.password.encode("UTF-8"), data, hashlib.sha1).digest()
        ).decode("UTF-8")

        headers["geofox-auth-signature"] = f"{signature}"
        headers["geofox-auth-user"] = self.username

        headers["Content-Type"] = "application/json"

        response = await self.websession.request(
            method,
            f"https://{self.host}{path}",
            data=data,
            **kwargs,
            headers=headers,
        )

        response_data: dict[str, Any] = await response.json(content_type=None)

        return_code_raw = response_data.get("returnCode")
        return_code = (
            ReturnCode(return_code_raw) if return_code_raw is not None else None
        )
        error_text = response_data.get("errorText")
        error_dev_info = response_data.get("errorDevInfo")

        if return_code != ReturnCode.OK:
            raise GTIError(return_code, error_text, error_dev_info)

        return response_data
