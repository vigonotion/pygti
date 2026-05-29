from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import ReturnCode


class GTIError(Exception):
    """An exception occured while using the GTI API."""

    def __init__(
        self,
        return_code: ReturnCode | None = None,
        error_text: str | None = None,
        error_dev_info: str | None = None,
    ) -> None:
        super().__init__(error_text or str(return_code))
        self.return_code = return_code
        self.error_text = error_text
        self.error_dev_info = error_dev_info


class GTIHTTPError(GTIError):
    """Raised when the GTI server returns an HTTP error status code."""

    def __init__(self, status_code: int, dev_info: str | None = None) -> None:
        super().__init__(error_text=f"HTTP {status_code}", error_dev_info=dev_info)
        self.status_code = status_code


class GTIBadRequestError(GTIHTTPError):
    """HTTP 400 — Invalid request (e.g. XML parser error or invalid IDs)."""

    def __init__(self, dev_info: str | None = None) -> None:
        super().__init__(400, dev_info)


class GTIUnauthorizedError(GTIHTTPError):
    """HTTP 401 — Authentication failed (e.g. invalid signature or IP not whitelisted)."""

    def __init__(self, dev_info: str | None = None) -> None:
        super().__init__(401, dev_info)


class GTIForbiddenError(GTIHTTPError):
    """HTTP 403 — Access not permitted."""

    def __init__(self, dev_info: str | None = None) -> None:
        super().__init__(403, dev_info)


class GTITooManyRequestsError(GTIHTTPError):
    """HTTP 429 — Too many requests per time unit."""

    def __init__(self, dev_info: str | None = None) -> None:
        super().__init__(429, dev_info)


class GTIInternalServerError(GTIHTTPError):
    """HTTP 500 — Programming error in the GTI backend."""

    def __init__(self, dev_info: str | None = None) -> None:
        super().__init__(500, dev_info)


class GTIServiceUnavailableError(GTIHTTPError):
    """HTTP 503 — Backend system unreachable."""

    def __init__(self, dev_info: str | None = None) -> None:
        super().__init__(503, dev_info)
