import base64
import contextlib
import hashlib
import hmac
import json
from collections.abc import Callable
from typing import Any

from aiohttp import ClientSession, ContentTypeError
from pydantic import BaseModel

from .exceptions import (
    GTIBadRequestError,
    GTIError,
    GTIForbiddenError,
    GTIHTTPError,
    GTIInternalServerError,
    GTIServiceUnavailableError,
    GTITooManyRequestsError,
    GTIUnauthorizedError,
)
from .models import ReturnCode

_HTTP_ERROR_MAP: dict[int, Callable[[str | None], GTIHTTPError]] = {
    400: GTIBadRequestError,
    401: GTIUnauthorizedError,
    403: GTIForbiddenError,
    429: GTITooManyRequestsError,
    500: GTIInternalServerError,
    503: GTIServiceUnavailableError,
}

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

        if response.status >= 400:
            dev_info: str | None = None
            with contextlib.suppress(json.JSONDecodeError, ContentTypeError):
                error_body = await response.json(content_type=None)
                if isinstance(error_body, dict):
                    dev_info = (
                        error_body.get("errorDevInfo")
                        if "errorDevInfo" in error_body
                        else error_body.get("message")
                    )
            if response.status in _HTTP_ERROR_MAP:
                raise _HTTP_ERROR_MAP[response.status](dev_info)
            raise GTIHTTPError(response.status, dev_info)

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
