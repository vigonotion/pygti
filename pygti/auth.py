from requests.auth import AuthBase
import base64
import hashlib
import hmac
import json


class GTIAuth(AuthBase):
    def __init__(self, gti, payload):
        self.gti = gti
        self.sig = base64.b64encode(
            hmac.new(
                gti.password.encode("UTF-8"),
                json.dumps(payload).encode("UTF-8"),
                hashlib.sha1,
            ).digest()
        )

    def __call__(self, req):
        req.headers["geofox-auth-signature"] = self.sig
        req.headers["geofox-auth-user"] = self.gti.username
        return req
