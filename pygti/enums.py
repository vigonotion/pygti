from enum import Enum


class CoordinateType(Enum):
    EPSG_4326 = 1
    EPSG_31467 = 2


class SDType(Enum):
    STATION = 1
    COORDINATE = 2
    ADDRESS = 3
    POI = 4
    UNKNOWN = 5


class FilterServiceType(Enum):
    ZUG = 1
    UBAHN = 2
    SBAHN = 3
    AKN = 4
    RBAHN = 5
    FERNBAHN = 6
    BUS = 7
    STADTBUS = 8
    METROBUS = 9
    SCHNELLBUS = 10
    NACHTBUS = 11
    EILBUS = 12
    AST = 13
    FAEHRE = 14
