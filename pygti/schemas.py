from datetime import datetime

import pytz
from voluptuous import All, In, Length, LengthInvalid, Range, Required, Schema

CoordinateType = In(["EPSG_4326", "EPSG_31467"])

SDType = In(["STATION", "COORDINATE", "ADDRESS", "POI", "UNKNOWN"])

Language = In(["de", "en"])

FilterType = In(["HVV_Listed", "NO_FILTER"])


class ModLength(Length):
    def __init__(self, min=None, max=None, msg=None, mod=None):
        super(self.__class__, self).__init__(min=min, max=max, msg=msg)
        self.mod = mod

    def __call__(self, v):
        super(self.__class__, self).__call__(v)
        if self.mod is not None and len(v) % self.mod != 0:
            raise LengthInvalid(
                self.msg or "length of value must be divisible by %s" % self.mod
            )
        return v


def DateTime(dt):
    dt = pytz.utc.localize(dt)
    return f"{dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]}{dt.strftime('%z')}"


# See 1.4 in gti docs
BaseRequestType = Schema({"language": Language, "filterType": FilterType})

FilterServiceType = In(
    [
        "ZUG",
        "UBAHN",
        "SBAHN",
        "AKN",
        "RBAHN",
        "FERNBAHN",
        "BUS",
        "STADTBUS",
        "METROBUS",
        "SCHNELLBUS",
        "NACHTBUS",
        "EILBUS",
        "AST",
        "FAEHRE",
    ]
)

AnnouncementFilterPlannedType = In(["ONLY_PLANNED", "ONLY_UNPLANNED", "NO_FILTER"])

TariffDetails = Schema(
    {
        "innerCity": bool,
        "cityTraffic": bool,
        "gratis": bool,
        "greaterArea": bool,
        "tariffZones": [int],
        "counties": [str],
        "rings": [str],
        "fareStage": bool,
        "fareStageNumber": int,
        "tariffNames": [str],
    }
)

Coordinate = Schema({"x": float, "y": float, "type": CoordinateType})

SDName = Schema(
    {
        "name": str,
        "city": str,
        "combinedName": str,
        "id": str,
        "type": SDType,
        "coordinate": Coordinate,
        "tariffDetails": TariffDetails,
        "serviceTypes": [str],
        "hasStationInformation": bool,
    }
)

CNRequest = Schema.extend(
    BaseRequestType,
    {
        "theName": SDName,
        "maxList": int,
        "maxDistance": int,
        "coordinateType": CoordinateType,
        "tariffDetails": bool,
        "allowTypeSwitch": bool,
    },
)

GTITime = Schema({"date": str, "time": str})

FilterEntry = Schema(
    {Required("serviceID"): str, "stationIDs": [str], "serviceName": str, "label": str}
)


DLRequest = Schema.extend(
    BaseRequestType,
    {
        "station": SDName,
        "stations": [SDName],
        "time": GTITime,
        "maxList": int,
        "maxTimeOffset": int,
        "allStationsInChangingNode": bool,
        "returnFilters": bool,
        "filter": [FilterEntry],
        "serviceTypes": [FilterServiceType],
        "useRealtime": bool,
    },
)

SIRequest = Schema.extend(BaseRequestType, {"station": SDName})

ContSearchByServiceId = Schema(
    {
        "serviceId": int,
        "lineKey": str,
        "plannedDepArrTime": GTITime,
        "additionalOffset": int,
    }
)

# kinds: GTI Docs say int but traffic on the website uses strings
# Same thing with the value of the penalty. All are strings
TariffInfoSelector = Schema({"tariff": str, "tariffRegions": bool, "kinds": [str]})
PenaltyName = In(
    [
        "ChangeEvent",
        "ExtraFare",
        "Walker",
        "AnyHandicap",
        "ToStartStationBy",
        "TimeRange",
        "ForVisitors",
        "desiredType",
        "DesiredLine",
    ]
)

Penalty = Schema({"name": PenaltyName, "value": str})

RealtimeType = In(["REALTIME", "PLANDATA", "AUTO"])

SimpleServiceType = In(
    [
        "BUS",
        "TRAIN",
        "SHIP",
        "FOOTPATH",
        "BICYCLE",
        "AIRPLANE",
        "CHANGE",
        "CHANGE_SAME_PLATFORM",
    ]
)

ServiceType = Schema(
    {"simpleType": SimpleServiceType, "shortInfo": str, "longInfo": str, "model": str}
)
GRRequest = Schema.extend(
    BaseRequestType,
    {
        Required("start"): SDName,
        Required("dest"): SDName,
        "via": SDName,
        "time": GTITime,
        "timeIsDeparture": bool,
        "numberOfSchedules": int,
        "tariffDetails": bool,
        "continousSearch": bool,
        "contSearchByServiceId": ContSearchByServiceId,
        "coordinateType": CoordinateType,
        "schedulesBefore": int,
        "schedulesAfter": int,
        "returnReduced": bool,
        "tariffInfoSelector": [TariffInfoSelector],
        "penalties": [Penalty],
        "returnPartialTickets": bool,
        "realtime": RealtimeType,
        "intermediateStops": bool,
        "useStationPosition": bool,
        "forcedStart": SDName,
        "forcedDest": SDName,
        "toStartBy": SimpleServiceType,
        "toDestBy": SimpleServiceType,
        "returnContSearchData": bool,
    },
)

LineModificationType = In(["MAIN", "SEQUENCE"])

LLRequest = Schema.extend(
    BaseRequestType,
    {
        "dataReleaseID": str,
        "modificationTypes": [LineModificationType],
        "withSublines": bool,
    },
)

ScheduleElementLight = Schema(
    {"departureStationId": str, "arrivalStationId": str, "lineId": str}
)

TariffRequest = Schema.extend(
    BaseRequestType,
    {
        Required("scheduleElements"): [ScheduleElementLight],
        Required("departure"): GTITime,
        Required("arrival"): GTITime,
        "returnReduced": bool,
        "returnPartialTickets": bool,
    },
)

IndividualProfileType = In(
    [
        "BICYCLE_NORMAL",
        "BICYCLE_RACING",
        "BICYCLE_QUIET_ROADS",
        "BICYCLE_MAIN_ROADS",
        "BICYCLE_BAD_WEATHER",
        "FOOT_NORMAL",
    ]
)

IndividualRouteRequest = Schema.extend(
    BaseRequestType,
    {
        "starts": [SDName],
        "dests": [SDName],
        "maxLength": int,
        "maxResults": int,
        "type": CoordinateType,
        "serviceType": SimpleServiceType,
        "profile": IndividualProfileType,
        "speed": str,
    },
)

ModificationType = In(["MAIN", "POSITION"])

LSRequest = Schema.extend(
    BaseRequestType,
    {
        "dataReleaseID": str,
        "modificationTypes": [ModificationType],
        "coordinateType": CoordinateType,
        "filterEquivalent": bool,
    },
)

BoundingBox = Schema({"lowerLeft": Coordinate, "upperRight": Coordinate})

VehicleType = In(
    [
        "REGIONALBUS",
        "METROBUS",
        "NACHTBUS",
        "SCHNELLBUS",
        "EILBUS",
        "AST",
        "SCHIFF",
        "U_BAHN",
        "S_BAHN",
        "R_BAHN",
        "A_BAHN",
        "F_BAHN",
    ]
)

VehicleMapRequest = Schema.extend(
    BaseRequestType,
    {
        "boundingBox": BoundingBox,
        "periodBegin": int,
        "periodEnd": int,
        "withoutCoords": bool,
        "coordinateType": CoordinateType,
        "vehicleTypes": [VehicleType],
        "realtime": bool,
    },
)

SIRequest = Schema({"station": SDName})

TimeRange = Schema({Required("begin"): DateTime, Required("end"): DateTime})

AnnouncementRequest = Schema.extend(
    BaseRequestType,
    {
        "names": [str],
        "timeRange": TimeRange,
        "full": bool,
        "filterPlanned": AnnouncementFilterPlannedType,
    },
)

PostalCodeRequest = Schema.extend(
    BaseRequestType,
    {
        "postalCode": Range(
            min=1000,
            max=99999,
            msg="value must be a valid german postal code (5 digits)",
        )
    },
)

TrackCoordinatesRequest = Schema.extend(
    BaseRequestType,
    {
        "coordinateType": CoordinateType,
        Required("stopPointKeys"): All([str], ModLength(min=2, mod=2)),
    },
)

TariffZoneNeighboursRequest = BaseRequestType

TLRequest = Schema.extend(BaseRequestType, {"stationKey": str})
