from .auth import Auth
from .const import *
from .schemas import (
    AnnouncementRequest,
    CNRequest,
    DLRequest,
    GRRequest,
    IndividualRouteRequest,
    LLRequest,
    LSRequest,
    PostalCodeRequest,
    SIRequest,
    TariffRequest,
    TariffZoneNeighboursRequest,
    TLRequest,
    TrackCoordinatesRequest,
    VehicleMapRequest,
)


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

    async def getRoute(self, payload):
        request = GRRequest(payload)
        response = await self.auth.request("post", ENDPOINT_GET_ROUTE, request)
        return await response.json()

    async def departureList(self, payload):
        request = DLRequest(payload)
        response = await self.auth.request("post", ENDPOINT_DEPARTURE_LIST, request)
        return await response.json()

    async def getIndividualRoute(self, payload):
        request = IndividualRouteRequest(payload)
        response = await self.auth.request(
            "post", ENDPOINT_GET_INDIVIDUAL_ROUTE, request
        )
        return await response.json()

    async def listLines(self, payload):
        request = LLRequest(payload)
        response = await self.auth.request("post", ENDPOINT_LIST_LINES, request)
        return await response.json()

    async def getTariff(self, payload):
        request = TariffRequest(payload)
        response = await self.auth.request("post", ENDPOINT_GET_TARIFF, request)
        return await response.json()

    async def listStations(self, payload):
        request = LSRequest(payload)
        response = await self.auth.request("post", ENDPOINT_LIST_STATIONS, request)
        return await response.json()

    async def getVehicleMap(self, payload):
        request = VehicleMapRequest(payload)
        response = await self.auth.request("post", ENDPOINT_GET_VEHICLE_MAP, request)
        return await response.json()

    async def getTrackCoordinates(self, payload):
        request = TrackCoordinatesRequest(payload)
        response = await self.auth.request(
            "post", ENDPOINT_GET_TRACK_COORDINATES, request
        )
        return await response.json()

    async def stationInformation(self, payload):
        request = SIRequest(payload)
        response = await self.auth.request(
            "post", ENDPOINT_GET_STATION_INFORMATION, request
        )
        return await response.json()

    async def getAnnouncements(self, payload):
        request = AnnouncementRequest(payload)
        response = await self.auth.request("post", ENDPOINT_GET_ANNOUNCEMENTS, request)
        return await response.json()

    async def checkPostalCode(self, payload):
        request = PostalCodeRequest(payload)
        response = await self.auth.request("post", ENDPOINT_CHECK_POSTAL_CODE, request)
        return await response.json()

    async def tariffZoneNeighbours(self, payload):
        request = TariffZoneNeighboursRequest(payload)
        response = await self.auth.request(
            "post", ENDPOINT_TARIFF_ZONE_NEIGHBOURS, request
        )
        return await response.json()

    async def ticketList(self, payload):
        request = TLRequest(payload)
        response = await self.auth.request("post", ENDPOINT_TICKET_LIST, request)
        return await response.json()
