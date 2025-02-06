import base64
import hashlib
import hmac
import json
from abc import ABC, abstractmethod


class AuthStrategy(ABC):
    """Base class for authentication strategies."""

    @abstractmethod
    def authenticate_request(self, headers: dict, payload: dict) -> None:
        """Modify headers and payload for authentication."""
        pass


class NoAuth(AuthStrategy):
    """No authentication strategy."""

    def authenticate_request(self, headers: dict, payload: dict) -> None:
        pass


class HMACAuth(AuthStrategy):
    """HMAC-based authentication strategy."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def authenticate_request(self, headers: dict, payload: dict) -> None:
        data = json.dumps(payload).encode("UTF-8")

        signature = base64.b64encode(
            hmac.new(self.password.encode("UTF-8"), data, hashlib.sha1).digest()
        ).decode("UTF-8")

        headers["geofox-auth-signature"] = signature
        headers["geofox-auth-user"] = self.username
