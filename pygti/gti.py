from pygti.request import Request
from .auth import AuthStrategy
from .const import (
    ENDPOINT_INIT,
    ENDPOINT_CHECK_NAME,
    ENDPOINT_GET_ROUTE,
    ENDPOINT_DEPARTURE_LIST,
    ENDPOINT_GET_INDIVIDUAL_ROUTE,
    ENDPOINT_LIST_LINES,
    ENDPOINT_GET_TARIFF,
    ENDPOINT_DEPARTURE_COURSE,
    ENDPOINT_LIST_STATIONS,
    ENDPOINT_GET_VEHICLE_MAP,
    ENDPOINT_GET_TRACK_COORDINATES,
    ENDPOINT_GET_STATION_INFORMATION,
    ENDPOINT_GET_ANNOUNCEMENTS,
    ENDPOINT_CHECK_POSTAL_CODE,
    ENDPOINT_TARIFF_ZONE_NEIGHBOURS,
    ENDPOINT_TARIFF_META_DATA,
    ENDPOINT_TICKET_LIST,
    ENDPOINT_SINGLE_TICKET_OPTIMIZER,
)
from .schemas import (
    AnnouncementRequest,
    BaseRequestType,
    CNRequest,
    DCRequest,
    DLRequest,
    GRRequest,
    IndividualRouteRequest,
    LLRequest,
    LSRequest,
    PCRequest,
    SingleTicketOptimizerRequest,
    StationInformationRequest,
    TariffRequestType,
    TariffZoneNeighboursRequest,
    TicketListRequest,
    TrackCoordinatesRequest,
    VehicleMapRequest,
)


class GTI:
    def __init__(self, auth_strategy: AuthStrategy, request: Request):
        self.auth_strategy = auth_strategy
        self.request = request

    async def init(self):
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_INIT, {}
        )
        return await response.json()

    async def checkName(self, payload):
        request = CNRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_CHECK_NAME, request
        )
        return await response.json()

    async def getRoute(self, payload):
        request = GRRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_GET_ROUTE, request
        )
        return await response.json()

    async def departureList(self, payload):
        request = DLRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_DEPARTURE_LIST, request
        )
        return await response.json()

    async def getIndividualRoute(self, payload):
        request = IndividualRouteRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_GET_INDIVIDUAL_ROUTE, request
        )
        return await response.json()

    async def listLines(self, payload):
        request = LLRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_LIST_LINES, request
        )
        return await response.json()

    async def getTariff(self, payload):
        request = TariffRequestType(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_GET_TARIFF, request
        )
        return await response.json()

    async def departureCourse(self, payload):
        request = DCRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_DEPARTURE_COURSE, request
        )
        return await response.json()

    async def listStations(self, payload):
        request = LSRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_LIST_STATIONS, request
        )
        return await response.json()

    async def getVehicleMap(self, payload):
        request = VehicleMapRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_GET_VEHICLE_MAP, request
        )
        return await response.json()

    async def getTrackCoordinates(self, payload):
        request = TrackCoordinatesRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_GET_TRACK_COORDINATES, request
        )
        return await response.json()

    async def stationInformation(self, payload):
        request = StationInformationRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_GET_STATION_INFORMATION, request
        )
        return await response.json()

    async def getAnnouncements(self, payload):
        request = AnnouncementRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_GET_ANNOUNCEMENTS, request
        )
        return await response.json()

    async def checkPostalCode(self, payload):
        request = PCRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_CHECK_POSTAL_CODE, request
        )
        return await response.json()

    async def tariffZoneNeighbours(self, payload):
        request = TariffZoneNeighboursRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_TARIFF_ZONE_NEIGHBOURS, request
        )
        return await response.json()

    async def tariffMetaData(self, payload):
        request = BaseRequestType(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_TARIFF_META_DATA, request
        )
        return await response.json()

    async def ticketList(self, payload):
        request = TicketListRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_TICKET_LIST, request
        )
        return await response.json()

    async def singleTicketOptimizer(self, payload):
        request = SingleTicketOptimizerRequest(payload)
        response = await self.request.request(
            self.auth_strategy, "post", ENDPOINT_SINGLE_TICKET_OPTIMIZER, request
        )
        return await response.json()
