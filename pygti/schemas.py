from voluptuous import Schema, Required, In

CoordinateType = In(["EPSG_4326", "EPSG_31467"])

SDType = In(["STATION", "COORDINATE", "ADDRESS", "POI", "UNKNOWN"])

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

CNRequest = Schema(
    {
        "theName": SDName,
        "maxList": int,
        "maxDistance": int,
        "coordinateType": CoordinateType,
        "tariffDetails": bool,
        "allowTypeSwitch": bool,
    }
)

GTITime = Schema({"date": str, "time": str})

FilterEntry = Schema(
    {Required("serviceID"): str, "stationIDs": [str], "serviceName": str, "label": str}
)


DLRequest = Schema(
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
    }
)

SIRequest = Schema({"station": SDName})
