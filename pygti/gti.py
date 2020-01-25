from .auth import Auth
from .const import *
from .schemas import *


class GTI:
    def __init__(self, auth):
        self.auth = auth

    async def init(self):
        response = await self.auth.request("post", ENDPOINT_INIT, {})
        return await response.json()

    async def checkName(self, payload):
        request = CNRequest(payload)
        response = await self.auth.request("post", ENDPOINT_CHECK_NAME, request)
        return await response.json()

    async def departureList(self, payload):
        request = DLRequest(payload)
        response = await self.auth.request("post", ENDPOINT_DEPARTURE_LIST, request)
        return await response.json()

    async def stationInformation(self, payload):
        request = SIRequest(payload)
        response = await self.auth.request(
            "post", ENDPOINT_GET_STATION_INFORMATION, request
        )
        return await response.json()
