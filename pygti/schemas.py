from voluptuous import Schema, Required, In

CoordinateType = In(["EPSG_4326", "EPSG_31467"])

SDType = In(["STATION", "COORDINATE", "ADDRESS", "POI", "UNKNOWN"])

Language = In(["de", "en"])

FilterType = In(["HVV_Listed", "NO_FILTER"])

# See 1.4 in gti docs
BaseRequestType = Schema(
    {"language": Language, "version": int, "filterType": FilterType,}
)

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
TariffInfoSelector = Schema({"tariff": str, "tariffRegions": bool, "kinds": [str],})
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

RealtimeType = In(["REALTIME", "PLANDATA","AUTO"])

SimpleServiceType = In(
    ["BUS", "TRAIN", "SHIP", "FOOTPATH", "BICYCLE", "AIRPLANE", "CHANGE"]
)

ServiceType = Schema(
    {"simpleType": SimpleServiceType, "shortInfo": str, "longInfo": str, "model": str,}
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
