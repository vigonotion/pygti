from abc import ABC, abstractmethod
from aiohttp import ClientConnectorError, ClientResponse, ClientSession

from pygti.auth import AuthStrategy
from pygti.const import GTI_DEFAULT_SERVER
from pygti.exceptions import (
    CannotConnect,
    CheckNameTooMany,
    CommunicationError,
    GTIError,
    InvalidAuth,
    RouteError,
)


class Request(ABC):
    """Base class for authentication strategies."""

    def __init__(self, server: str):
        self.server = server

    @abstractmethod
    async def request(
        self,
        auth_strategy: AuthStrategy,
        method: str,
        path: str,
        payload=None,
        **kwargs,
    ) -> ClientResponse:
        pass


class AiohttpRequest(Request):
    """Class to make authenticated requests to the geofox API."""

    def __init__(
        self,
        websession: ClientSession,
        server: str = GTI_DEFAULT_SERVER,
    ):
        """Initialize authentication."""
        super().__init__(server)
        self.websession = websession

    async def request(
        self,
        auth_strategy: AuthStrategy,
        method: str,
        path: str,
        payload=None,
        **kwargs,
    ) -> ClientResponse:
        """Make a request with authentication."""
        headers = kwargs.get("headers", {}).copy()
        payload = payload or {}

        payload.update({"version": 54})

        # Use the authentication strategy
        auth_strategy.authenticate_request(headers, payload)

        try:
            response = await self.websession.request(
                method,
                f"{self.server}/{path}",
                json=payload,
                **kwargs,
                headers=headers,
            )

            data = await response.json()
            return_code = data.get("returnCode")
            error_text = data.get("errorText")
            error_dev_info = data.get("errorDevInfo")

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

            return response

        except ClientConnectorError as error:
            raise CannotConnect(error)
