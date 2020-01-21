import requests

from .auth import GTIAuth
from .const import *
from .schemas import *


class GTI:
    def __init__(self, username, password, server="http://api-test.geofox.de"):
        self.username = username
        self.password = password
        self.server = server

    def request(self, uri, payload):
        payload.update({"version": 37})
        res = requests.post(uri, json=payload, auth=GTIAuth(self, payload))
        return res.json()

    def init(self):
        return self.request(self.server + ENDPOINT_INIT, {})

    def checkName(self, payload):
        request = CNRequest(payload)
        return self.request(self.server + ENDPOINT_CHECK_NAME, request)

    def departureList(self, payload):
        request = DLRequest(payload)
        return self.request(self.server + ENDPOINT_DEPARTURE_LIST, request)

    def stationInformation(self, payload):
        request = SIRequest(payload)
        return self.request(self.server + ENDPOINT_GET_STATION_INFORMATION, request)
