from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import ReturnCode


class GTIError(Exception):
    """An exception occured while using the GTI API."""

    def __init__(
        self,
        return_code: ReturnCode | None,
        error_text: str | None,
        error_dev_info: str | None,
    ) -> None:
        self.return_code = return_code
        self.error_text = error_text
        self.error_dev_info = error_dev_info
