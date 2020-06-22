"""
This file was generated automatically by xsd-to-vol. Do not edit.
"""

from datetime import datetime

import pytz
from voluptuous import All, In, Length, Required, Schema, Url


def DateTime(dt):
    dt = pytz.utc.localize(dt)
    return f"{dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]}{dt.strftime('%z')}"


"""TariffMetaDataRequest


"""

TariffMetaDataRequest = Schema({})

"""TariffZoneNeighboursRequest

Requests all HVV zones and their zone neighbours.


"""

TariffZoneNeighboursRequest = Schema({})

"""TariffRequest


"""

TariffRequest = Schema({})

"""GRRequest


"""

GRRequest = Schema({})

"""ErrorResponse

An error occurred on the server side. This type of Response will only be send in combination with the http
				status code 401 and 403.


"""

ErrorResponse = Schema({})

"""SingleTicketOptimizerRequestLine

id: str  (None - None)
name: str  (None - None)

"""

SingleTicketOptimizerRequestLine = Schema({"id": str, "name": str})

"""SingleTicketOptimizerRequestStation

id: str  (None - None)
name: str  (None - None)

"""

SingleTicketOptimizerRequestStation = Schema({"id": str, "name": str})

"""SingleTicketOptimizerRequestTrip

start: SingleTicketOptimizerRequestStation  (None - None)
destination: SingleTicketOptimizerRequestStation  (None - None)
line: SingleTicketOptimizerRequestLine  (None - None)
vehicleType: str  (None - None)

"""

SingleTicketOptimizerRequestTrip = Schema(
    {
        "start": SingleTicketOptimizerRequestStation,
        "destination": SingleTicketOptimizerRequestStation,
        "line": SingleTicketOptimizerRequestLine,
        "vehicleType": str,
    }
)

"""TariffRegions

regions: str  (None - unbounded)

"""

TariffRegions = Schema({"regions": [str]})

"""TariffOptimizerRegions

Regions to be covered by tickets

zones: TariffRegions  (0 - unbounded)
rings: TariffRegions  (0 - unbounded)
counties: TariffRegions  (0 - unbounded)

"""

TariffOptimizerRegions = Schema(
    {"zones": [TariffRegions], "rings": [TariffRegions], "counties": [TariffRegions]}
)

"""TariffCounty

contains information about a tariff county

id: str Unique identifier for this tariff county (None - None)
label: str label of the tariff county (None - None)

"""

TariffCounty = Schema({"id": str, "label": str})

"""TimePeriod

The ticket is valid within this period.

begin: str Begin of the period. Format: HH:mm (This might contain hour values > 24, in case of next day) (None - None)
end: str End of the period. Format: HH:mm (This might contain hour values > 24, in case of next day) (None - None)

"""

TimePeriod = Schema({"begin": str, "end": str})

"""TariffZone

zone: str Contains a HVV fare zone. (None - None)
ring: str Contains a HVV fare ring. (None - None)
neighbours: str The neighbouring zones of the current zone. (None - unbounded)

"""

TariffZone = Schema({"zone": str, "ring": str, "neighbours": [str]})

"""Link

label: str additional summazied informations about the
						linked content (e.g. "Ersatzfahrplan"). (None - None)
url: str Defines a link providing further information
						about a actual notice. (None - None)

"""

Link = Schema({"label": str, "url": str})

"""TimeRange

begin: DateTime Begin of TimeRange. (Null means "open end") (0 - None)
end: DateTime End of TimeRange. (Null means "open end") (0 - None)

"""

TimeRange = Schema({"begin": DateTime, "end": DateTime})

"""StationLight

Represents a light version of a station.

id: str The unique id of the station (None - None)
name: str The name of the station. (0 - None)

"""

StationLight = Schema({"id": str, "name": str})

"""TariffRegionList

Holds a list of tariff regions (e.g. tariff-zones, tariff-rings).

regions: str list of crossed tariff regions. (0 - unbounded)

"""

TariffRegionList = Schema({"regions": [str]})

"""ScheduleElementLight

One element of a schedule with from/to station and line IDs. This is a lighter form of a ScheduleElement.
				ScheduleElementLights are allways public transport elements (no footpathes allowed). Departure and arrival
				are allways at a station.

departureStationId: str ID of the departure station. (None - None)
arrivalStationId: str ID of the arrival station. (None - None)
lineId: str ID of the line used between departure and arrivel station. (None - None)

"""

ScheduleElementLight = Schema(
    {"departureStationId": str, "arrivalStationId": str, "lineId": str}
)

"""Property

Property which can be part of InitRequest and InitResponse. Is needed for transferring properties from server to
				client.

key: str The key which identifies a property. (None - None)
value: str The value of a property which is identified by the key. (0 - None)

"""

Property = Schema({"key": str, "value": str})

"""Ticket

The ticket information.
        DEPRECATED since API Version 13
				replaced by "tariffInfos"

price: float The price of the ticket. (None - None)
reducedPrice: float The reduced price for online shopping.
						* since version 16 (0 - None)
currency: str The currency of the price. Default is Euro. Default: EUR (0 - None)
type: str The type information of the ticket. e.g. Einzelfahrt (None - None)
level: str The level information of the ticket. e.g. Nahbereich (None - None)
tariff: str The tariff information of the ticket. e.g. HVV (None - None)
range: str The stations of the ticket. (None - None)
ticketRemarks: str Additional information about ticket. For example if it is only valid on a part of the trip.
						* since version 18 (0 - None)

"""

Ticket = Schema(
    {
        "price": float,
        "reducedPrice": float,
        "currency": str,
        "type": str,
        "level": str,
        "tariff": str,
        "range": str,
        "ticketRemarks": str,
    }
)

"""TariffInfoSelector

Returns Ticketinfos (in schedule) for each of this tariffs and kinds, if the given tariff and kind is valid on
				the returned schedule.

tariff: str tariff of HVV or SH? "all" will select all tariffs. Default: HVV (0 - None)
tariffRegions: bool also return tariff regions (tariffzones, rings, counties)? Default: true (0 - None)
kinds: int Returns Ticketinfos (in schedule) for each of this tariff kinds, if the kind is valid on the returned
						schedule. An empty list will return cards of every valid kind. (0 - unbounded)

"""

TariffInfoSelector = Schema({"tariff": str, "tariffRegions": bool, "kinds": [int]})

"""Penalty

The penalties for a GRRequest.

name: str The name of the penalty. (None - None)
value: str The value of the penalty. In most cases a single int value.
						Exception:
						- DesiredType - string:int (e.g. bus:10)
						- DesiredLine - string,...,string:int (e.g. U1,S21,U3:3) (None - None)

"""

Penalty = Schema({"name": str, "value": str})

"""DLFilterEntry

Filter for DLRequest.
				* since Version 20

serviceID: str ID of the Departure's service. Either serviceID or stationID must be filled in for Request. (0 - None)
stationIDs: str IDs of stations of which one must be on the journey after (before in case of departure=false) the reference
            station. Either serviceID or stationIDs must be filled for Request. (0 - unbounded)
label: str A string that discribes the direction for the user. This field could be empty in DLRequest (server will not
						evaluate this field) and is allways filled in the list of possible filter entries in DLResponse. (0 - None)
serviceName: str A string that represents the public name of the service. (0 - None)

"""

DLFilterEntry = Schema(
    {"serviceID": str, "stationIDs": [str], "label": str, "serviceName": str}
)

"""GTITime

date: str The date as string. Format: dd.mm.yyyy (None - None)
time: str The time as string. Format: hh:mm (None - None)

"""

GTITime = Schema({"date": str, "time": str})

"""ContSearchByServiceId

serviceId: int the service id of the first/last trip part with
						vehicle (1 - None)
lineKey: str the line key of the first/last trip part with
						vehicle (1 - None)
plannedDepArrTime: GTITime the planned departure/arrival time at the
						start/dest station (1 - None)
additionalOffset: int an additional offset for the footway to the
						start/dest; negative in the dest case (1 - None)

"""

ContSearchByServiceId = Schema(
    {
        Required("serviceId"): int,
        Required("lineKey"): str,
        Required("plannedDepArrTime"): GTITime,
        Required("additionalOffset"): int,
    }
)

"""Attribute

title: str The title of the attribute. (None - None)
isPlanned: bool Is the attribute planned? (None - None)
value: str A text to describe the attribute. (None - None)
types: str Type of an attribute. Currently used attribute types are:
						-NORMAL:
                The default attribute type for simple text attributes.
						-ANNOUNCEMENT:
                Attribute for announcement messages
						-REALTIME:
                Informations about missed connections, cancelled journeys, etc.
						-DIRECTION_NAME:
                Indicates that the attribute value defines a direction name.
						-ENTRY_PROHIBITED:
                Indicates that no passenger can enter the vehicle on that station.
						-EXIT_PROHIBITED:
                Indicates that the passengers can't exit the vehicle on this station.
						-STOP_ON_DEMAND:
                Indicates that the vehicle does not necessarily hold on that station.
                The vehicle holds only if a passenger wants to exit.
						-PLATFORM:
                Indicates that the attribute value defines the platform number where the vehicle holds.
						-NOCHANGE:
                Indicates that the change (from fussweg.asc) is not a real change.
                The passenger can stay in the same vehicle.
						-POSITION_FRONT:
                Indicates that the attribute value defines the optimal position in the train (In this case: front).
						-POSITION_BACK:
                Indicates that the attribute value defines the optimal position in the train (In this case: back).
						-POSITION_MIDDLE:
                Indicates that the attribute value defines the optimal position in the train (In this case: middle).
            These types could be supplemented with new ones without creating a new interface version.
            Clients should be prepared to handle unknown types.
						* since version 3 (0 - unbounded)

"""

Attribute = Schema({"title": str, "isPlanned": bool, "value": str, "types": [str]})

"""TariffDetails

Some detailed information about a tariff.

innerCity: bool  (None - None)
city: bool  (None - None)
cityTraffic: bool  (None - None)
gratis: bool  (None - None)
greaterArea: bool  (None - None)
tariffZones: int  (0 - unbounded)
regions: int  (0 - unbounded)
counties: str  (0 - unbounded)
rings: str  (0 - unbounded)
fareStage: bool  (None - None)
fareStageNumber: int  (None - None)
tariffNames: str  (0 - unbounded)
uniqueValues: bool  (None - None)

"""

TariffDetails = Schema(
    {
        "innerCity": bool,
        "city": bool,
        "cityTraffic": bool,
        "gratis": bool,
        "greaterArea": bool,
        "tariffZones": [int],
        "regions": [int],
        "counties": [str],
        "rings": [str],
        "fareStage": bool,
        "fareStageNumber": int,
        "tariffNames": [str],
        "uniqueValues": bool,
    }
)

"""BaseResponseType


"""

BaseResponseType = Schema({})

"""TariffZoneNeighboursResponse

Response of the TariffZoneNeighboursRequest, which contains all HVV zones.

tariffZones: TariffZone List of all zones. (None - unbounded)

"""

TariffZoneNeighboursResponse = Schema.extend(
    BaseResponseType, {"tariffZones": [TariffZone]}
)

"""PCResponse

isHVV: bool Whether the postal code intersects the HVV
									area (None - None)

"""

PCResponse = Schema.extend(BaseResponseType, {"isHVV": bool})

"""InitResponse

beginOfService: str The time when the current timetable started. (None - None)
endOfService: str The time when the current timetable will end. (None - None)
id: str The ID of the geofox release. (None - None)
dataId: str The ID of the data. (None - None)
buildDate: str The build date of the Geofox release which is overwritten by build date of the data. (None - None)
buildTime: str The build time of the Geofox release which is overwritten by build time of the data. (None - None)
buildText: str The build text/name of the data release. (None - None)
version: str The version. (None - None)
properties: Property An optional list of properties which the client requested. (0 - unbounded)

"""

InitResponse = Schema.extend(
    BaseResponseType,
    {
        "beginOfService": str,
        "endOfService": str,
        "id": str,
        "dataId": str,
        "buildDate": str,
        "buildTime": str,
        "buildText": str,
        "version": str,
        "properties": [Property],
    },
)

"""TariffExtraFareType

Specifies wether the route requires any type of ExtraFare
"""

TariffExtraFareType = In(["NO", "POSSIBLE", "REQUIRED"])

"""SingleTicketOptimizerRequestRoute

trip: SingleTicketOptimizerRequestTrip  (None - unbounded)
departure: DateTime Time of departure (None - None)
arrival: DateTime Time of arrival (None - None)
tariffRegions: TariffOptimizerRegions Regions that need to be covered by tickets (None - None)
singleTicketTariffLevelId: int  (None - None)
extraFareType: TariffExtraFareType Specifies wether the tickets have some type of extra fare (None - None)

"""

SingleTicketOptimizerRequestRoute = Schema(
    {
        "trip": [SingleTicketOptimizerRequestTrip],
        "departure": DateTime,
        "arrival": DateTime,
        "tariffRegions": TariffOptimizerRegions,
        "singleTicketTariffLevelId": int,
        "extraFareType": TariffExtraFareType,
    }
)

"""TariffPersonType

- ALL: Alle
- ADULT: Erwachsene
- ELDERLY: Senioren
- APPRENTICE: Auszubildende
- PUPIL: Schüler
- STUDENT: Studenten
- CHILD: Kinder
"""

TariffPersonType = In(
    ["ALL", "ADULT", "ELDERLY", "APPRENTICE", "PUPIL", "STUDENT", "CHILD"]
)

"""TicketRegionType

type of a tariff region
- RING: tariff
level is based on tariff rings (A, B, ...).
- ZONE: tariff level is
based on tariff zones (000, 101, ...).
- COUNTY tariff level is
based on counties (SE, WL, ...).
- GH_ZONE: tariff level is
"Großbereich Hamburg" + X Zones. (since version 14).
"""

TicketRegionType = In(["RING", "ZONE", "COUNTY", "GH_ZONE"])

"""TariffOptimizerTicket

tariffKindId: int  (None - None)
tariffKindLabel: str  (0 - None)
tariffLevelId: int  (None - None)
tariffLevelLabel: str  (0 - None)
tariffRegions: str Regions covered by this ticket (None - unbounded)
regionType: TicketRegionType  (None - None)
count: int  (None - None)
extraFare: bool  (None - None)
personType: TariffPersonType  (None - None)
centPrice: int  (None - None)

"""

TariffOptimizerTicket = Schema(
    {
        "tariffKindId": int,
        "tariffKindLabel": str,
        "tariffLevelId": int,
        "tariffLevelLabel": str,
        "tariffRegions": [str],
        "regionType": TicketRegionType,
        "count": int,
        "extraFare": bool,
        "personType": TariffPersonType,
        "centPrice": int,
    }
)

"""SingleTicketOptimizerResponse

Response of the TariffOptimizer

tickets: TariffOptimizerTicket Tickets the user has to buy for the requested route (0 - unbounded)

"""

SingleTicketOptimizerResponse = Schema.extend(
    BaseResponseType, {"tickets": [TariffOptimizerTicket]}
)

"""TicketType

is ticket a single ticket or a season ticket?
"""

TicketType = In(["OCCASIONAL_TICKET", "SEASON_TICKET"])

"""TariffKind

Contains information about a tariff kind

id: int Unique identifier for this tariff kind (None - None)
label: str label of the tariff kind (None - None)
requiresPersonType: bool Contains information if further information about the type of person using this card is needed (used in
						tariff optimizer) Default: false (0 - None)
ticketType: TicketType is ticket a single ticket or a season ticket? (0 - None)
levelCombinations: int Contains information about which levels this kind can be combined with (0 - unbounded)

"""

TariffKind = Schema(
    {
        "id": int,
        "label": str,
        "requiresPersonType": bool,
        "ticketType": TicketType,
        "levelCombinations": [int],
    }
)

"""ValidityDayType

- WEEKDAY: Mo-Fr
- WEEKEND: Saturday, Sunday, public holidays
"""

ValidityDayType = In(["WEEKDAY", "WEEKEND"])

"""ValidityPeriod

Contains information about the validity of this ticket.

day: ValidityDayType The DayType of the validityPeriod (WEEKDAY, WEEKEND) (None - None)
timeValidities: TimePeriod The ticket is valid within this period. (0 - unbounded)

"""

ValidityPeriod = Schema({"day": ValidityDayType, "timeValidities": [TimePeriod]})

"""PersonType

- ALL: Alle
- ELDERLY: Senioren
- APPRENTICE: Auszubildende
- PUPIL: Schüler
- STUDENT: Studenten
- CHILD: Kinder
"""

PersonType = In(["ALL", "ELDERLY", "APPRENTICE", "PUPIL", "STUDENT", "CHILD"])

"""PersonInfo

Contains information for how many people of a specific type of person the card is for.

personType: PersonType Contains the information about the specific type of person. (0 - None)
personCount: int Contains information for how many people the card is for. (0 - None)

"""

PersonInfo = Schema({"personType": PersonType, "personCount": int})

"""DiscountType

- NONE: kein Rabatt
- ONLINE: Onlinerabatt
- SOCIAL: Sozialrabatt
"""

DiscountType = In(["NONE", "ONLINE", "SOCIAL"])

"""TicketClass

- NONE: classes are not relevant for this ticket.
- SECOND: 2nd class
- FIRST: 1st class
- SCHNELL: ticket includes "Schnellbus" extra fare.
"""

TicketClass = In(["NONE", "SECOND", "FIRST", "SCHNELL"])

"""TicketListTicketVariant

Contains informations about one variant of a ticket from the TicketListRequest.

ticketId: int Contains a unique ID for this ticket variant.
						In case of HVV this contains the unique 8 digit HVV ticket ID. (None - None)
kaNummer: int The KA-Nummer of this ticket. Might be null if unknown. (0 - None)
price: float The ticket price. (None - None)
currency: str The currency of the price. Default is Euro. Default: EUR (0 - None)
ticketClass: TicketClass Travel class of this ticket (None - None)
discount: DiscountType included discount in this ticket (None - None)
validityBegin: DateTime The validity start date of the tickets tariff data. (None - None)
validityEnd: DateTime The validity end date of the tickets tariff data. (None - None)

"""

TicketListTicketVariant = Schema(
    {
        "ticketId": int,
        "kaNummer": int,
        "price": float,
        "currency": str,
        "ticketClass": TicketClass,
        "discount": DiscountType,
        "validityBegin": DateTime,
        "validityEnd": DateTime,
    }
)

"""ElevatorState

Enumeration with all possible elevator states.
"""

ElevatorState = In(["READY", "OUTOFORDER", "UNKNOWN"])

"""ElevatorButtonType

Enumeration with all possible elevator button
types.
"""

ElevatorButtonType = In(["BRAILLE", "ACUSTIC", "COMBI", "UNKNOWN"])

"""Elevator

lines: str The elevator serves the platform for the lines
						listed here (0 - unbounded)
label: str The label of the elevator. (0 - None)
cabinWidth: int The width of the cabin (0 - None)
cabinLength: int The width of the cabin (0 - None)
doorWidth: int The width of the cabin door (0 - None)
description: str A description of the elevator (0 - None)
elevatorType: str The type of the elevator (0 - None)
buttonType: ElevatorButtonType The type of the buttons (0 - None)
state: ElevatorState The state of the elevator (0 - None)
cause: str Cause of the the elevator's state (0 - None)

"""

Elevator = Schema(
    {
        "lines": [str],
        "label": str,
        "cabinWidth": int,
        "cabinLength": int,
        "doorWidth": int,
        "description": str,
        "elevatorType": str,
        "buttonType": ElevatorButtonType,
        "state": ElevatorState,
        "cause": str,
    }
)

"""PartialStation

lines: str The partial station is reached by these lines
						listed here.
						If this field is not set, all not otherwise mentioned
						lines that reach the station do that through this partial station (0 - unbounded)
stationOutline: Url The outline of the partial station. (0 - None)
elevators: Elevator The elevators at this partial station. (0 - unbounded)

"""

PartialStation = Schema(
    {"lines": [str], "stationOutline": Url, "elevators": [Elevator]}
)

"""StationInformationResponse

partialStations: PartialStation The station might be divided in different
									parts. These parts are listed here. (0 - unbounded)
lastUpdate: GTITime The last time the dynamic elevator data where
									updated (0 - None)

"""

StationInformationResponse = Schema.extend(
    BaseResponseType, {"partialStations": [PartialStation], "lastUpdate": GTITime}
)

"""AnnouncementFilterPlannedType

Enumeration of all possible types for filtering
the announcements concerning their planned-flag
- NO_FILTER -
default, nothing is filtered
- ONLY_PLANNED - only announcements
about planned events are returned
- ONLY_UNPLANNED - only
announcements about unplanned events are returned
"""

AnnouncementFilterPlannedType = In(["NO_FILTER", "ONLY_PLANNED", "ONLY_UNPLANNED"])

"""LocationType

Enumeration with possible types of a location.
"""

LocationType = In(["SINGLE_LINE", "ALL_LINES_OF_CARRIER", "COMPLETE_NET"])

"""LineModificationType

type of modification.
MAIN: Modification of one of
the main informations about the object (e.g.
name, carrier name).
SEQUENCE: Modification of the main station sequence.
"""

LineModificationType = In(["MAIN", "SEQUENCE"])

"""ModificationType

type of modification.
MAIN: modification of one of
the main informations about the object (e.g.
name, city).
POSITION:
object got new coordinates.
"""

ModificationType = In(["MAIN", "POSITION"])

"""VehicleType

type of list station entry.
AST: Anruf-Sammel-Taxi
U_BAHN: U-Bahn Hamburg
S_BAHN: S-Bahn Hamburg
A_BAHN: AKN Eisenbahn
R_BAHN: Regionalbahn (R10, R30, ...)
F_BAHN: Fernbahn (IC, ICE, ...)
* since API version 17
"""

VehicleType = In(
    [
        "REGIONALBUS",
        "METROBUS",
        "NACHTBUS",
        "SCHNELLBUS",
        "XPRESSBUS",
        "AST",
        "SCHIFF",
        "U_BAHN",
        "S_BAHN",
        "A_BAHN",
        "R_BAHN",
        "F_BAHN",
        "EILBUS",
    ]
)

"""SublineListEntry

One entry of the subline list

sublineNumber: str The internal number of this subline. This number
						may change
						frequently on each data release. (None - None)
vehicleType: VehicleType Type of vehicle of this subline. (None - None)
stationSequence: StationLight The station sequence of the subline as station
						ids. (0 - unbounded)

"""

SublineListEntry = Schema(
    {
        "sublineNumber": str,
        "vehicleType": VehicleType,
        "stationSequence": [StationLight],
    }
)

"""SegmentSelector

Return stations before or after the given station
or return all stations.
-BEFORE: return stations before the given
stations on the given line
-AFTER: return stations after the given
stations on the given line
-ALL: return all stations on the given
line
"""

SegmentSelector = In(["BEFORE", "AFTER", "ALL"])

"""TariffRegionType

type of a tariff region
- ZONE: tariff level is
	based on tariff zones (000, 101, ...).
- GH_ZONE: tariff level is
	"Großbereich Hamburg" + X Zones. (since version 14)
- RING: tariff
	level is based on tariff rings (A, B, ...).
- COUNTY tariff level is
	based on counties (SE, WL, ...).
- GH tariff level is
	based on Großbereich Hamburg/Hamburg AB.
- NET tariff level is
	valid in complete tariff net.
- ZG tariff level is
	based on payment borders (Zahlgrenzen).
- STADTVERKEHR tariff level is
	based on limits for city tickets.
"""

TariffRegionType = In(
    ["ZONE", "GH_ZONE", "RING", "COUNTY", "GH", "NET", "ZG", "STADTVERKEHR"]
)

"""RequiredRegionType

Contains information about the needed information regarding the region type

type: TariffRegionType holds information about the type that is required (None - None)
count: int holds information about how many regions of the type are required (None - None)

"""

RequiredRegionType = Schema({"type": TariffRegionType, "count": int})

"""TariffLevel

Contains information about a tariff level

id: int Unique identifier for this tariff level (None - None)
label: str label of the tariff level (None - None)
requiredRegionType: RequiredRegionType Describes what additional region information is needed to buy the ticket. (e.g. 2 Zones or 1 County) (None - None)

"""

TariffLevel = Schema(
    {"id": int, "label": str, "requiredRegionType": RequiredRegionType}
)

"""TariffMetaDataResponse

Contains tariff related meta data

tariffKinds: TariffKind Contains the different tariff kinds (0 - unbounded)
tariffLevels: TariffLevel Contains the different tariff levels information (0 - unbounded)
tariffCounties: TariffCounty Contains the different tariff counties information (0 - unbounded)
tariffZones: TariffZone Contains the different tariff zones (0 - unbounded)
tariffRings: str Contains the different tariff rings (0 - unbounded)

"""

TariffMetaDataResponse = Schema.extend(
    BaseResponseType,
    {
        "tariffKinds": [TariffKind],
        "tariffLevels": [TariffLevel],
        "tariffCounties": [TariffCounty],
        "tariffZones": [TariffZone],
        "tariffRings": [str],
    },
)

"""TicketListTicketInfos

Contains infos of a ticket.

tariffKindID: int id of the tariff kind (Kartenart). (None - None)
tariffKindLabel: str name of the tariff kind (e.g. Einzelkarte). (None - None)
tariffLevelID: int id of the tariff level (Tarifstufe). (None - None)
tariffLevelLabel: str name of the tariff level (e.g. Kurzstrecke). (None - None)
tariffGroupID: int id of the tariff group. (0 - None)
tariffGroupLabel: str name of the tariff group (e.g. Allgemeine Zeitkarten). (0 - None)
regionType: TariffRegionType if this is not null, the specified TicketInfo needs this type of additional TariffRegionInfos.
						* since version 14 (0 - None)
selectableRegions: int The number of selectable regions with this ticket. (for example with "2 Tarifzonen" this would be 2) Default: 0 (0 - None)
requiredStartStation: bool Holds information if the ticket needs start station information to verify validity. Default: false (None - None)
personInfos: PersonInfo Contains list of information for how many people of a specific type of person the card is for. (0 - unbounded)
validityPeriods: ValidityPeriod Contains information about the validity of this ticket. (0 - unbounded)
variants: TicketListTicketVariant Contains information about one variant of this ticket. (for example 2nd class and 1st class) (0 - unbounded)

"""

TicketListTicketInfos = Schema(
    {
        "tariffKindID": int,
        "tariffKindLabel": str,
        "tariffLevelID": int,
        "tariffLevelLabel": str,
        "tariffGroupID": int,
        "tariffGroupLabel": str,
        "regionType": TariffRegionType,
        "selectableRegions": int,
        "requiredStartStation": bool,
        "personInfos": [PersonInfo],
        "validityPeriods": [ValidityPeriod],
        "variants": [TicketListTicketVariant],
    }
)

"""TicketListResponse

Response of the TicketListRequest, which contains all HVV Tickets.

ticketInfos: TicketListTicketInfos List of all tickets. (None - unbounded)

"""

TicketListResponse = Schema.extend(
    BaseResponseType, {"ticketInfos": [TicketListTicketInfos]}
)

"""TariffRegionInfo

Holds informations about a tariff region (e.g. tariff-zones, tariff-rings).

regionType: TariffRegionType Type of tariff region (e.g. tariff-zone, tariff-ring).
						(could be null if there is no TicketInfo of type GH_ZONE). (None - None)
alternatives: TariffRegionList altanatives of crossed tariff regions. Because stations could belong to more than one tariff region, there
						could be different possible list of crossed regions for the same route. (0 - unbounded)

"""

TariffRegionInfo = Schema(
    {"regionType": TariffRegionType, "alternatives": [TariffRegionList]}
)

"""TicketInfo

Holds detail ticket informations.

tariffKindID: int id of the tariff kind (Kartenart). (None - None)
tariffKindLabel: str name of the tariff kind (e.g. Einzelkarte). (None - None)
tariffLevelID: int id of the tariff level (Tarifstufe). (None - None)
tariffLevelLabel: str name of the tariff level (e.g. Kurzstrecke). (None - None)
tariffGroupID: int id of the tariff group. (0 - None)
tariffGroupLabel: str name of the tariff group (e.g. Allgemeine Zeitkarten). (0 - None)
basePrice: float base ticket price (without extra fare). (None - None)
extraFarePrice: float additional extra fare ticket price. (0 - None)
reducedBasePrice: float reduced base ticket price (without extra fare).
						* since version 16 (0 - None)
reducedExtraFarePrice: float reduced additional extra fare ticket price.
						* since version 16 (0 - None)
currency: str The currency of the price. Default is Euro. Default: EUR (0 - None)
regionType: TariffRegionType if this is not null, the specified TicketInfo needs this type of additional TariffRegionInfos.
						* since version 14 (0 - None)
notRecommended: bool If set to true, this ticket is valid but not recommended.
            * since version 32 Default: false (0 - None)
shopLinkRegular: str The link to the shop, where you could buy this ticket as a regular ticket.
            * since version 32 (0 - None)
shopLinkExtraFare: str The link to the shop, where you could buy this ticket as an extra fare ticket.
            * since version 32 (0 - None)

"""

TicketInfo = Schema(
    {
        "tariffKindID": int,
        "tariffKindLabel": str,
        "tariffLevelID": int,
        "tariffLevelLabel": str,
        "tariffGroupID": int,
        "tariffGroupLabel": str,
        "basePrice": float,
        "extraFarePrice": float,
        "reducedBasePrice": float,
        "reducedExtraFarePrice": float,
        "currency": str,
        "regionType": TariffRegionType,
        "notRecommended": bool,
        "shopLinkRegular": str,
        "shopLinkExtraFare": str,
    }
)

"""ShopType

- AST: Anruf-Sammel-Taxi
"""

ShopType = In(["AST"])

"""ShopInfo

Information about the shop, where a ticket could be bought.

shopType: ShopType Type of Shop (for example Anruf-Sammel-Taxi) (1 - 1)
url: str URL of the responsible ticket shop. (1 - 1)

"""

ShopInfo = Schema({Required("shopType"): ShopType, Required("url"): str})

"""RealtimeType

Configures the consideration of realtime informations during route calculation.
-PLANDATA: only return a result based on plandata.
-REALTIME: only return a result based on realtime data.
-AUTO: The plandata result (schedules) will allways be returned. Realtime result
(realtimeSchedules) will be returned if it is different from plandata result.
* since version 19
"""

RealtimeType = In(["PLANDATA", "REALTIME", "AUTO"])

"""IndividualProfileType

Configures requests for routes by different profiles.
* since version 25
"""

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

"""SimpleServiceType

Enumeration with all simple types of services
* BICYCLE since API version 17
"""

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

"""ServiceType

The complex type of a Service. Includes the simple type and additional information.

simpleType: SimpleServiceType The simple type of a Service, like BUS or TRAIN. (None - None)
shortInfo: str A short information about the vehicle (e.g. Schnellbus). More information see properties in geofox. (0 - None)
longInfo: str More detailled information about the vehicle (e.g. Niederflur-Schnellbus). More information
            see properties in geofox. (0 - None)
model: str The specific model of the vehicle if applicable and available. * since API version 24 (0 - None)

"""

ServiceType = Schema(
    {"simpleType": SimpleServiceType, "shortInfo": str, "longInfo": str, "model": str}
)

"""LineListEntry

One entry of the line list

id: str The unique id of an entry (None - None)
name: str Name of the entry. Is null if the line was
						deleted. (0 - None)
carrierNameShort: str Short name of the carrier. Is null if the line
						was deleted. (0 - None)
carrierNameLong: str Long name of the carrier. Is null if the line
						was deleted. (0 - None)
sublines: SublineListEntry List of sublines. Is null if no sublines were
						requested or if the line
						was deleted. (0 - unbounded)
exists: bool This field is false if the line is deleted. Default: true (0 - None)
type: ServiceType The type of the service. For Example: BUS, TRAIN
						with optional additional information. (None - None)

"""

LineListEntry = Schema(
    {
        "id": str,
        "name": str,
        "carrierNameShort": str,
        "carrierNameLong": str,
        "sublines": [SublineListEntry],
        "exists": bool,
        "type": ServiceType,
    }
)

"""LLResponse

The response for LLRequest with a list of lines.

dataReleaseID: str result was created on this data release. (0 - None)
lines: LineListEntry List of lines. This list could be empty if
									there is no line fitting
									to the given filter settings. (0 - unbounded)

"""

LLResponse = Schema.extend(
    BaseResponseType, {"dataReleaseID": str, "lines": [LineListEntry]}
)

"""Service

The service with type and a name.

name: str The name of the service. For Example: S1, U3, 101, etc. (None - None)
direction: str The direction where the service is headed. (0 - None)
directionId: int The id of the direction. Forward (1), backward (6). (0 - None)
origin: str The origin where the service comes from (opposite of direction).
						* since version 19 (0 - None)
type: ServiceType The type of the service. For Example: BUS, TRAIN with optional additional information. (None - None)
id: str The id of a service. Is neccessary for TariffRequest. This is NOT the service-id, but the line key
						* since version 4 (0 - None)

"""

Service = Schema(
    {
        "name": str,
        "direction": str,
        "directionId": int,
        "origin": str,
        "type": ServiceType,
        "id": str,
    }
)

"""IndividualTrack

time: int The time of the IndividualTrack in minutes. (None - None)
length: int The length of the IndividualTrack in km. (None - None)
type: SimpleServiceType The type of the IndividualTrack. (None - None)

"""

IndividualTrack = Schema({"time": int, "length": int, "type": SimpleServiceType})

"""FilterServiceType

To filter departures by service type.
* since version 22
"""

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
        "XPRESSBUS",
        "AST",
        "FAEHRE",
        "EILBUS",
    ]
)

"""CoordinateType

type of a coordinate
-EPSG_4326 wgs84
-EPSG_31466 Gauss-Kruger zone 2
-EPSG_31467 Gauss-Kruger zone 3
-EPSG_31468 Gauss-Kruger zone 4
-EPSG_31469 Gauss-Kruger zone 5
for explanation of types: http://www.epsg-registry.org/ currently
        only wgs84 and Gauss-Kruger zone 3 are supported
"""

CoordinateType = In(
    ["EPSG_4326", "EPSG_31466", "EPSG_31467", "EPSG_31468", "EPSG_31469"]
)

"""VehicleMapPath

description of a path from a given start to a destination with coordinates and properties.

track: float Coordinates of the path, 2 makes one coordinate, coordinateType is declared in "coordinateType" (4 - unbounded)
coordinateType: CoordinateType Type of the coordinates (None - None)

"""

VehicleMapPath = Schema(
    {Required("track"): All([float], Length(min=4)), "coordinateType": CoordinateType}
)

"""TrackCoordinatesResponse

response for TrackCoordinatesRequest

trackIDs: str The IDs of the tracks in tracks (1 - unbounded)
tracks: VehicleMapPath The requested coordinates (1 - unbounded)

"""

TrackCoordinatesResponse = Schema.extend(
    BaseResponseType,
    {
        Required("trackIDs"): All([str], Length(min=1)),
        Required("tracks"): All([VehicleMapPath], Length(min=1)),
    },
)

"""PathSegment

startStopPointKey: str the Key of the startstoppoint of this segment (None - None)
endStopPointKey: str the Key of the deststoppoint of this segment (None - None)
startStationName: str the name of the startstation of this segment (None - None)
startStationKey: str the Key of the startstation of this segment (None - None)
startDateTime: int timestamp - this segment begins at the first
						coordinate of the track at this start date/time (None - None)
endStationName: str the name of the endstation of this segment (None - None)
endStationKey: str the Key of the endstation of this segment (None - None)
endDateTime: int timestamp - this segment ends at the last
						coordinate of the track at this end date/time (None - None)
track: VehicleMapPath The actual coordinate-Track (None - None)
destination: str The Destination Display on the Station for this
						Vehicle (None - None)
realtimeDelay: int realtime delay informations in minutes (None - None)
isFirst: bool determins if this is the First segment of a
						Journey (None - None)
isLast: bool determins if
						this is the Last segment of a
						Journey (None - None)

"""

PathSegment = Schema(
    {
        "startStopPointKey": str,
        "endStopPointKey": str,
        "startStationName": str,
        "startStationKey": str,
        "startDateTime": int,
        "endStationName": str,
        "endStationKey": str,
        "endDateTime": int,
        "track": VehicleMapPath,
        "destination": str,
        "realtimeDelay": int,
        "isFirst": bool,
        "isLast": bool,
    }
)

"""Journey

journeyID: str Fahrt ID - Unique identifier for this journey (None - None)
line: Service unique ID of the line that is doing this journey (None - None)
vehicleType: VehicleType journey is done with this type of vehicle (None - None)
realtime: bool data is based on realtime informations (None - None)
segments: PathSegment each journey is splitted in one segment between
						two stations (0 - unbounded)

"""

Journey = Schema(
    {
        "journeyID": str,
        "line": Service,
        "vehicleType": VehicleType,
        "realtime": bool,
        "segments": [PathSegment],
    }
)

"""VehicleMapResponse

response for VehicleMapRequest

journeys: Journey informations about the journeys inside the
									given bounding box and period (1 - unbounded)

"""

VehicleMapResponse = Schema.extend(
    BaseResponseType, {Required("journeys"): All([Journey], Length(min=1))}
)

"""Coordinate

the coordinate of a location with x and y value

x: float the x value or longitude of the coordinate (None - None)
y: float the y value or latitude of the coordinate (None - None)
type: CoordinateType type of a coordinate.
						default is wgs84 Default: EPSG_4326 (0 - None)

"""

Coordinate = Schema({"x": float, "y": float, "type": CoordinateType})

"""BoundingBox

represents a Box by defining the lower-left and
				the upper-right Corner.
				Usecases: limiting a request, describing the
				hull of a geometry, ...

lowerLeft: Coordinate the coordinate at lower-left Corner (None - None)
upperRight: Coordinate the coordinate at upper-right Corner (None - None)

"""

BoundingBox = Schema({"lowerLeft": Coordinate, "upperRight": Coordinate})

"""StationListEntry

One entry of the station list

id: str the unique id of an entry (None - None)
name: str name of the entry. is null if the station was
						deleted. (0 - None)
city: str entry belongs to this city. is null if the station was deleted. (0 - None)
combinedName: str combination of name and city field. In order to reduce response size, this field is null if the combined
						name can be build
						by concating city and name in the form: city + ", " + name (0 - None)
shortcuts: str list of short names for station. (could be empty
						or null if there is no shortcut) (0 - unbounded)
aliasses: str list of aliasses for station. (could be empty or
						null if there is no alias) (0 - unbounded)
vehicleTypes: VehicleType types of vehicles that depart at this station. (0 - unbounded)
coordinate: Coordinate the coordinate of an SDName object. (could be
						null!) (0 - None)
exists: bool this field is false if the station is deleted. Default: true (0 - None)

"""

StationListEntry = Schema(
    {
        "id": str,
        "name": str,
        "city": str,
        "combinedName": str,
        "shortcuts": [str],
        "aliasses": [str],
        "vehicleTypes": [VehicleType],
        "coordinate": Coordinate,
        "exists": bool,
    }
)

"""LSResponse

The response for LSRequest with a list of stations.

dataReleaseID: str result was created on this data release. (0 - None)
stations: StationListEntry List of stations. This list could be empty if there is no station fitting to the given filter settings. (0 - unbounded)

"""

LSResponse = Schema.extend(
    BaseResponseType, {"dataReleaseID": str, "stations": [StationListEntry]}
)

"""Path

description of a path from a given start to a destination with coordinates and properties.

track: Coordinate Coordinates of the path (2 - unbounded)
attributes: str Attributes of the track
						* since version 25 (0 - unbounded)

"""

Path = Schema(
    {Required("track"): All([Coordinate], Length(min=2)), "attributes": [str]}
)

"""ExtraFareType

type of extra fare
- NO extra fare is not possible or required
- POSSIBLE extra fare is possible (optional first class ticket)
- REQUIRED extra fare is mandatory
"""

ExtraFareType = In(["NO", "POSSIBLE", "REQUIRED"])

"""TariffInfo

Holds detail tariff informations.

tariffName: str The name of the tariff (HVV, SH). (None - None)
tariffRegions: TariffRegionInfo crossed tariffregions of different types (zones, rings, counties). (0 - unbounded)
extraFareType: ExtraFareType is extra fare possible? if yes, is it mandatory? Default: NO (0 - None)
ticketInfos: TicketInfo detailed informations about the possible and valid tickets (0 - unbounded)
ticketRemarks: str Additional information about ticket. For example if it is only valid on a part of the trip.
						* since version 18 (0 - None)

"""

TariffInfo = Schema(
    {
        "tariffName": str,
        "tariffRegions": [TariffRegionInfo],
        "extraFareType": ExtraFareType,
        "ticketInfos": [TicketInfo],
        "ticketRemarks": str,
    }
)

"""TariffResponse

tariffInfos: TariffInfo Tariff informations. (0 - unbounded)

"""

TariffResponse = Schema.extend(BaseResponseType, {"tariffInfos": [TariffInfo]})

"""SDType

type of location.
* UNKNOWN since version 6
"""

SDType = In(["UNKNOWN", "STATION", "ADDRESS", "POI", "COORDINATE"])

"""SDName

type for representation of starts and destinations

name: str string which can be the name of station, address or poi (0 - None)
city: str the city of the location (0 - None)
combinedName: str combination of name and city field.
						* since version 6 (0 - None)
id: str the unique id of a SDName object (0 - None)
type: SDType the type of a SDName object, type can be:
						UNKNOWN, STATION , ADDRESS, POI, COORDINATE.
						Unknown type is only for requests. Default: UNKNOWN (0 - None)
coordinate: Coordinate the coordinate of a SDName object (0 - None)
tariffDetails: TariffDetails Detailed information about the tariff. (0 - None)
serviceTypes: str Type of vehicles that stops at this station. (Only filled on SDType Station)
						* since version 16 (0 - unbounded)
hasStationInformation: bool Are additional information about the station available? Can be retrieved by StationInformationRequest
						* since version 28 (0 - None)

"""

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

"""Location

type: LocationType SINGLE_LINE : the announcement concerns a single
						line that is given with the 'line' field
						ALL_LINES_OF_CARRIER: the
						name field contains the short name of the concerned carrier
						COMPLETE_NET: the name field contains the concerned net (e.g.
						"HVV") Default: SINGLE_LINE (0 - None)
name: str Description of the location.
						* Isnt filled if
						there are line elements. (0 - None)
line: Service The concerned line.
						* Only filled if type is
						SINGLE_LINE.
						* 'full' must be set to true
						to fill this element.
						*
						since version 22 (0 - None)
begin: SDName First Station that is affected on the given
						line.
						* Only filled if type is SINGLE_LINE.
						* 'full' must be set to
						true
						to fill this element.
						* since version 22 (0 - None)
end: SDName Last Station that is affected on the given line.
						* Only filled if type is SINGLE_LINE.
						* 'full' must be set to true
						to fill this element.
						* since version 22 (0 - None)
bothDirections: bool if set to true, this announcement concerns both
						directions of the line.
						* Only relevant if type is SINGLE_LINE.
						*
						'full' must be set to true to fill this element.
						* since version 22 Default: true (0 - None)

"""

Location = Schema(
    {
        "type": LocationType,
        "name": str,
        "line": Service,
        "begin": SDName,
        "end": SDName,
        "bothDirections": bool,
    }
)

"""Announcement

id: str a unique announcement id. Announcement updates
						result in a new announcement with a new ID. (0 - None)
version: int a version-number to keep track of the history (0 - None)
summary: str a summarized description text if available (e.g.
						"Streik"). (0 - None)
locations: Location a list of concerned locations. this could be a
						single line, all lines of
						one carrier or the complete net. (1 - unbounded)
description: str A description text of the announcement. (None - None)
links: Link Links providing further information, if
						available. (0 - unbounded)
publication: TimeRange Publication Window for announcement.
						* since
						version 22 (None - None)
validities: TimeRange Overall inclusive period of applicability of
						announcement.
						* 'full' must be set to true to fill this element.
						*
						since version
						22 (None - unbounded)
lastModified: DateTime Date/Time of last modification of this
						announcement.
						* since version 22 (None - None)
planned: bool Is the event planned?
						* since Version 30 (0 - None)
reason: str The reason of the announcement, in key form.
						Takes at the moment only the following values:
						- UNDEFINED_PROBLEM
						- ROADWORKS
						- CONGESTION
						- SPECIAL_EVENT
						- SLIPPERINESS
						-
						POLICE_REQUEST
						- FIRE_BRIGADE_SAFETY_CHECKS
						- STATION_OVERRUN
						-
						SERVICE_FAILURE
						- ROAD_CLOSED
						- VEHICLE_ON_THE_LINE
						- ACCIDENT
						-
						DEMONSTRATION
						- STAFF_ABSENCE
						- BOMB_ALERT
						- LOW_WATER_LEVEL
						-
						ROUTE_BLOCKAGE
						- ROUGH_SEA
						* since Version 30 (0 - None)

"""

Announcement = Schema(
    {
        "id": str,
        "version": int,
        "summary": str,
        Required("locations"): All([Location], Length(min=1)),
        "description": str,
        "links": [Link],
        "publication": TimeRange,
        "validities": [TimeRange],
        "lastModified": DateTime,
        "planned": bool,
        "reason": str,
    }
)

"""AnnouncementResponse

announcements: Announcement A list of announcements that fits to the
									requested parameters. (0 - unbounded)
lastUpdate: DateTime Time of last announcement update. (None - None)

"""

AnnouncementResponse = Schema.extend(
    BaseResponseType, {"announcements": [Announcement], "lastUpdate": DateTime}
)

"""CourseElement

A course element with from- and to-station, departure time, duration, platform and optional the path.

fromStation: SDName contains the departure station of the course element. In order to reduce traffic on mobile devices, only the
						unique combinedName will be returned. The completely filled SDName object can be requested by CNRequest. (None - None)
fromPlatform: str The scheduled platform (Gleis) of this from-station. If no platform info is available this
						element will be null. (0 - None)
fromRealtimePlatform: str The realtime platform (Gleis) of this from-station. If no realtime platform info is available this element
						will be null.
						* since version 21 (0 - None)
toStation: SDName contains the arrival station of the course element. In order to reduce traffic on mobile devices, only the
						unique combinedName will be returned. The completely filled SDName object can be requested by CNRequest. (None - None)
toPlatform: str The scheduled platform (Gleis) of this to-station. If no platform info is available this element will be null. (0 - None)
toRealtimePlatform: str The realtime platform (Gleis) of this to-station. If no realtime platform info is available this element
						will be null.
						* since version 21 (0 - None)
model: str The specific model type of the vehicle if applicable and available.
						* since API version 24 (0 - None)
depTime: DateTime The departure time of the course element. (None - None)
arrTime: DateTime The arrival time of the course element. (None - None)
depDelay: int Realtime departure delay in seconds (if available).
						* since version 19 (0 - None)
arrDelay: int Realtime arrival delay in seconds (if available).
						* since version 19 (0 - None)
fromExtra: bool realtime flag to mark an additional from stop to those of the intended schedule.
						* since version 19 Default: false (0 - None)
fromCancelled: bool realtime flag to mark a cancelled from stop.
						* since version 19 Default: false (0 - None)
toExtra: bool realtime flag to mark an additional to stop to those of the intended schedule.
						* since version 19 Default: false (0 - None)
toCancelled: bool realtime flag to mark a cancelled to stop.
						* since version 19 Default: false (0 - None)
attributes: Attribute A list with additional textual informations about this leg.
						* since version 23 (0 - unbounded)
path: Path The (optional) path between fromStation and toStation of this course element. Will only be filled if the
						flag showPath in the request is set to true and a path is defined for the course. (0 - 1)

"""

CourseElement = Schema(
    {
        "fromStation": SDName,
        "fromPlatform": str,
        "fromRealtimePlatform": str,
        "toStation": SDName,
        "toPlatform": str,
        "toRealtimePlatform": str,
        "model": str,
        "depTime": DateTime,
        "arrTime": DateTime,
        "depDelay": int,
        "arrDelay": int,
        "fromExtra": bool,
        "fromCancelled": bool,
        "toExtra": bool,
        "toCancelled": bool,
        "attributes": [Attribute],
        "path": Path,
    }
)

"""DCResponse

The response for a DCRequest with a list of CourseElements.

courseElements: CourseElement The list with the course elements. Will be empty in case of an error or if it is the last station
									(followingStations=true) or the first station (followingStations=false) (0 - unbounded)
extra: bool realtime flag to mark additional journeys to those of the intended schedule.
									* since version 19 Default: false (0 - None)
cancelled: bool realtime flag to mark cancelled journeys.
									* since version 19 Default: false (0 - None)
attributes: Attribute A list with additional textual informations about the returned journey.
									* since version 23 (0 - unbounded)

"""

DCResponse = Schema.extend(
    BaseResponseType,
    {
        "courseElements": [CourseElement],
        "extra": bool,
        "cancelled": bool,
        "attributes": [Attribute],
    },
)

"""BaseSchedule

A schedule from start to dest with a list of legs as ScheduleElements.

routeId: int The id of the route. (None - None)
start: SDName The start of the schedule. (None - None)
dest: SDName The destination of the schedule. (None - None)
time: int The whole time (in minutes) the journey takes. (None - None)
footpathTime: int The whole time for all footpaths in the journey. (None - None)
tickets: Ticket DEPRECATED since API Version 13
						replaced by "tariffInfos" (None - unbounded)
tariffInfos: TariffInfo Tariff informations for this schedule.
						* select which tariff infos should be returned with the request field "tariffInfoSelection"
						* since version 13 (0 - unbounded)

"""

BaseSchedule = Schema(
    {
        "routeId": int,
        "start": SDName,
        "dest": SDName,
        "time": int,
        "footpathTime": int,
        "tickets": [Ticket],
        "tariffInfos": [TariffInfo],
    }
)

"""IndividualRoute

start: SDName Start of the individual route (one of the starts from request) (None - None)
dest: SDName Destination of the individual route (one of the dests from request) (None - None)
path: Path Coordinate sequence that describes the path of the route
						* optional since version 25, replaced by paths (0 - None)
paths: Path List of paths with attributes
						* since version 21 (0 - unbounded)
length: int length of the route in meters (None - None)
time: int estimated time to use individual route in seconds (None - None)
serviceType: SimpleServiceType type of individual route (eg. footpath) Default: FOOTPATH (None - None)

"""

IndividualRoute = Schema(
    {
        "start": SDName,
        "dest": SDName,
        "path": Path,
        "paths": [Path],
        "length": int,
        "time": int,
        "serviceType": SimpleServiceType,
    }
)

"""IndividualRouteResponse

response for IndividualRouteRequest

routes: IndividualRoute List of individual route results (1 - unbounded)

"""

IndividualRouteResponse = Schema.extend(
    BaseResponseType, {Required("routes"): All([IndividualRoute], Length(min=1))}
)

"""Departure

A departure with line, timeOffset and direction.

line: Service The line which departs. (None - None)
timeOffset: int The scheduled time in minutes when the line will depart/arrive.
						This value could be negative on delayed trains! (None - None)
delay: int realtime delay in seconds.
						* since version 19 (0 - None)
extra: bool realtime flag to mark additional journeys to those of the intended schedule.
						* since version 19 Default: false (0 - None)
cancelled: bool realtime flag to mark cancelled journeys.
						* since version 19 Default: false (0 - None)
serviceId: int A unique ID for each journey (Fahrt-ID)
						* since version 7 (0 - None)
station: SDName contains the station of the desired changing node for this departure. Is only filled if
            allStationsInChangingNode in request is true. In order to reduce traffic on mobile devices, only the
            unique combinedName will be returned. The completely filled SDName object can be requested by CNRequest.
						* since version 7 (0 - None)
platform: str The scheduled platform (Gleis) of this hold. If no platform info is available this element will be null.
						* since version 11 (0 - None)
realtimePlatform: str The realtime platform (Gleis) of this hold. If no realtime platform info is available this element
            will be null.
						* since version 21 (0 - None)
attributes: Attribute A list with additional textual informations about this journey.
						* since version 23 (0 - unbounded)

"""

Departure = Schema(
    {
        "line": Service,
        "timeOffset": int,
        "delay": int,
        "extra": bool,
        "cancelled": bool,
        "serviceId": int,
        "station": SDName,
        "platform": str,
        "realtimePlatform": str,
        "attributes": [Attribute],
    }
)

"""DLResponse

The response for a DLRequest with a list of Departures.

time: GTITime The time when the departure list is requested. (None - None)
departures: Departure The resulting list of departures or arrivals. (0 - unbounded)
filter: DLFilterEntry A list of possible values for DLFilterEntries for the given request. Will be filled if
                  'returnFilters' in request is set to true!
									* since Version 20 (0 - unbounded)
serviceTypes: FilterServiceType A list of servicetypes that serves this station.
									* since version 22 (0 - unbounded)

"""

DLResponse = Schema.extend(
    BaseResponseType,
    {
        "time": GTITime,
        "departures": [Departure],
        "filter": [DLFilterEntry],
        "serviceTypes": [FilterServiceType],
    },
)

"""RegionalSDName

distance: int The distance from the coordinate sent in the
                request to this SDName. The client has to know the coordinate. (0 - None)
time: int The travel time from the coordinate to this SDName. (0 - None)

"""

RegionalSDName = Schema.extend(SDName, {"distance": int, "time": int})

"""CNResponse

The response for a CNRequest with a list of SDNames.

results: RegionalSDName The list with the SDName objects. (0 - unbounded)

"""

CNResponse = Schema.extend(BaseResponseType, {"results": [RegionalSDName]})

"""JourneySDName

arrTime: GTITime The arrival time for this location. In most cases only one of dep- and arrTime will be used. (0 - None)
depTime: GTITime The departure time for this location (0 - None)
arrDelay: int Realtime arrival delay in seconds (if available).
								* since version 19 (0 - None)
depDelay: int Realtime departure delay in seconds (if available).
								* since version 19 (0 - None)
extra: bool realtime flag to mark additional stops to those of the intended schedule.
								* since version 19 Default: false (0 - None)
cancelled: bool realtime flag to mark cancelled stops.
								* since version 19 Default: false (0 - None)
attributes: Attribute A list with attributes. (0 - unbounded)
platform: str The scheduled platform (Gleis) of this hold. If no platform info is available this element will be null.
								* since version 11 (0 - None)
realtimePlatform: str The realtime platform (Gleis) of this hold. If no realtime platform info is available this element
                will be null.
								* since version 21 (0 - None)

"""

JourneySDName = Schema.extend(
    SDName,
    {
        "arrTime": GTITime,
        "depTime": GTITime,
        "arrDelay": int,
        "depDelay": int,
        "extra": bool,
        "cancelled": bool,
        "attributes": [Attribute],
        "platform": str,
        "realtimePlatform": str,
    },
)

"""ScheduleElement

One element of a schedule with from/to SDNames, departure/arrival times and line

from: JourneySDName The leg starts here. (None - None)
to: JourneySDName The leg ends here. (None - None)
line: Service The line/service which is used for this leg. (None - None)
paths: Path A list of possible paths from start to destination of this element.
						* since version 2 (0 - unbounded)
attributes: Attribute A list with attributes. (0 - unbounded)
extra: bool realtime flag to mark additional journeys to those of the intended schedule.
						* since version 19 Default: false (0 - None)
cancelled: bool realtime flag to mark cancelled journeys.
						* since version 19 Default: false (0 - None)
intermediateStops: JourneySDName A list of all intermediate stops between start and end station.
						* since version 24 (0 - unbounded)
serviceId: int the service-id of the journey
						* since version 29 (0 - None)
shopInfo: ShopInfo Information about the shop, where a ticket for this journey could be bought. (0 - unbounded)

"""

ScheduleElement = Schema(
    {
        "from": JourneySDName,
        "to": JourneySDName,
        "line": Service,
        "paths": [Path],
        "attributes": [Attribute],
        "extra": bool,
        "cancelled": bool,
        "intermediateStops": [JourneySDName],
        "serviceId": int,
        "shopInfo": [ShopInfo],
    }
)

"""Schedule

scheduleElements: ScheduleElement The legs between start and dest. (0 - unbounded)
contSearchBefore: ContSearchByServiceId cont-search data for a possible earlier schedule
								* since version 29 (0 - None)
contSearchAfter: ContSearchByServiceId cont-search data for a possible later schedule
								* since version 29 (0 - None)

"""

Schedule = Schema.extend(
    BaseSchedule,
    {
        "scheduleElements": [ScheduleElement],
        "contSearchBefore": ContSearchByServiceId,
        "contSearchAfter": ContSearchByServiceId,
    },
)

"""GRResponse

The response for a GRRequest with a list of schedules.

schedules: Schedule A list of schedules with all legs. Realtime-Informations where not considered to
									calculate this schedules. (0 - unbounded)
realtimeSchedules: Schedule A list of schedules with all legs. This schedules where calculated under consideration of realtime
									data. Type of realtime consideration could be configured by realtime field in request.
									* since version 19 (0 - unbounded)
realtimeAffected: bool Returns true if the realtime result differes from plandata result.
									* since version 19 Default: false (0 - None)
individualTrack: IndividualTrack Informations about an individual track (footpath, bike) for comparison to the public transport route.
									* since version 19 (0 - None)

"""

GRResponse = Schema.extend(
    BaseResponseType,
    {
        "schedules": [Schedule],
        "realtimeSchedules": [Schedule],
        "realtimeAffected": bool,
        "individualTrack": IndividualTrack,
    },
)

"""FilterType

Enumeration with all possible filter types.
-NO_FILTER: No filter for the result activated.
-HVV_LISTED: Return only stations, lines etc. belonging to HVV.
"""

FilterType = In(["NO_FILTER", "HVV_LISTED"])

"""BaseRequestType

language: str Language in which the server will respond. (de/en) Default: de (0 - None)
version: int Used version of GeofoxThinInterface on Client. Default: 1 (0 - None)
filterType: FilterType Sets the filter for the result. Default: NO_FILTER (None - None)

"""

BaseRequestType = Schema({"language": str, "version": int, "filterType": FilterType})

"""SingleTicketOptimizerRequest

Request for the TariffOptimizer

withReturnJourney: bool Specifies whether the tickets should also be valid for the return journey (None - None)
numberOfAdults: int Number of traveling adults (None - None)
numberOfChildren: int Number of traveling children (None - None)
tickets: TariffOptimizerTicket Tickets owned by user (0 - unbounded)
route: SingleTicketOptimizerRequestRoute The route for which a fare is searched (None - None)

"""

SingleTicketOptimizerRequest = Schema.extend(
    BaseRequestType,
    {
        "withReturnJourney": bool,
        "numberOfAdults": int,
        "numberOfChildren": int,
        "tickets": [TariffOptimizerTicket],
        "route": SingleTicketOptimizerRequestRoute,
    },
)

"""TicketListRequest

request a list of all HVV tickets.

stationKey: str The key of the station as used in Geofox (e.g. Master:12345) (0 - 1)

"""

TicketListRequest = Schema.extend(BaseRequestType, {"stationKey": str})

"""TrackCoordinatesRequest

request the coordinates for tracks

coordinateType: CoordinateType The Projection
									in that the result should be
									projected Default: EPSG_4326 (0 - None)
stopPointKeys: str The keys of the stopPoints; in blocks of 2; each block identifies
									a track (2 - unbounded)

"""

TrackCoordinatesRequest = Schema.extend(
    BaseRequestType,
    {
        "coordinateType": CoordinateType,
        Required("stopPointKeys"): All([str], Length(min=2)),
    },
)

"""VehicleMapRequest

request All Vehicles(and its Journey) in a
				specified Area at a specified period

boundingBox: BoundingBox requested area (None - None)
periodBegin: int timestamp begin of period (None - None)
periodEnd: int timestamp end of period (None - None)
withoutCoords: bool whether the response should not contain
									coordinates (None - None)
coordinateType: CoordinateType The Projection
									in that the result should be
									projected Default: EPSG_4326 (0 - None)
vehicleTypes: VehicleType requested types of vehicles (bus, s-bahn,...) (0 - unbounded)
realtime: bool consider realtime informations (0 - None)

"""

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

"""StationInformationRequest

station: SDName The station to get additional information
									about (None - None)

"""

StationInformationRequest = Schema.extend(BaseRequestType, {"station": SDName})

"""PCRequest

postalCode: int The postal code to check for intersection
									with the HVV area (None - None)

"""

PCRequest = Schema.extend(BaseRequestType, {"postalCode": int})

"""AnnouncementRequest

names: str Names of lines or carriers for which
									announcements are requested. (0 - unbounded)
timeRange: TimeRange the time range for which announcements are
									requested (0 - None)
full: bool If true, the result will contain detailed
									location and validity informations Default: false (0 - None)
filterPlanned: AnnouncementFilterPlannedType Should and how the announcements are to be
									filtered concerning their planned flag.
									* since Version 30 (0 - None)

"""

AnnouncementRequest = Schema.extend(
    BaseRequestType,
    {
        "names": [str],
        "timeRange": TimeRange,
        "full": bool,
        "filterPlanned": AnnouncementFilterPlannedType,
    },
)

"""LLRequest

List Lines Request. Returns a filtered list of
				lines.

withSublines: bool Indicates whether the sublines should be
									returned too.
									Enabling this flag can increase the amount of
									data. (None - None)
dataReleaseID: str return all modified lines since this release.
									this request will return all lines if this field is null. (0 - None)
modificationTypes: LineModificationType result only contains lines that are modified
									on one of the given
									types.
									Only fields that belongs to the
									requested types are filled in
									result.
									if this field is
									null/empty, all modifications will be
									considered. (0 - unbounded)

"""

LLRequest = Schema.extend(
    BaseRequestType,
    {
        "withSublines": bool,
        "dataReleaseID": str,
        "modificationTypes": [LineModificationType],
    },
)

"""LSRequest

List Stations Request. Returns a filtered list of stations.

dataReleaseID: str return all modified stations since this release. this request will return all stations if this field
									is null. (0 - None)
modificationTypes: ModificationType result only contains stations that are modified on one of the given types. Only fields that belongs
									to the requested types are filled in result. if this field is null/empty, all modifications will
									be considered. (0 - unbounded)
coordinateType: CoordinateType The type of the coordinate which the server should use in the response. Default: EPSG_4326 (0 - None)
filterEquivalent: bool In Geofox bus stops and train stations does not belong together to one station. For example the subway
									station "Niendorf Nord" and the bus station "U Niendorf Nord" are two different stations. With
									parameter "filterEquivalent" on true those stations will be merged to one station with vehicle types
									of both and with the name of the train station.
									* since API version 17 Default: false (0 - None)

"""

LSRequest = Schema.extend(
    BaseRequestType,
    {
        "dataReleaseID": str,
        "modificationTypes": [ModificationType],
        "coordinateType": CoordinateType,
        "filterEquivalent": bool,
    },
)

"""DCRequest

Departure course request. Get a list of positions related to a given Departure.

lineKey: str The key (string) of the line. For Example:
									HHA-U:U1_HHA-U, DB-EFZ:A3_DB-EFZ_Z, VHH:569_VHH etc. (None - None)
station: SDName contains the station for this departure (relates to line/direction/time) In order to reduce traffic
									on mobile devices, only the name/ID is needed/used. (None - None)
time: DateTime The departure date/time for this journey of the given line/direction/station. If the serviceId is set,
									only the date is relevant. (None - None)
direction: str The direction where the line is headed. (0 - None)
origin: str The origin where the line comes from. (0 - None)
serviceId: int A unique ID for the journey (Fahrt-ID). either serviceId or direction has to be set. Default: -1 (0 - None)
segments: SegmentSelector Defines whether the course starting from the given station to the end is shown (AFTER) or the portion
									from the beginning until the given station (BEFORE) or all stations (ALL). Default: ALL (0 - None)
showPath: bool Defines whether the coordinate path is returned together with the textual information of the course.
									Default is false. Default: false (0 - None)
coordinateType: CoordinateType The type of the coordinate which the server should use in the response. Default: EPSG_4326 (0 - None)

"""

DCRequest = Schema.extend(
    BaseRequestType,
    {
        "lineKey": str,
        "station": SDName,
        "time": DateTime,
        "direction": str,
        "origin": str,
        "serviceId": int,
        "segments": SegmentSelector,
        "showPath": bool,
        "coordinateType": CoordinateType,
    },
)

"""InitRequest

properties: Property An optional list of properties (only key has to be set). The server will response the properties
									(including the value) which are defined here. (0 - unbounded)

"""

InitRequest = Schema.extend(BaseRequestType, {"properties": [Property]})

"""IndividualRouteRequest

request for calculating an individual route (eg. footpath)

starts: SDName List of possible start positions. There will be calculated the shorted path from every start to
                  its nearest destinations. If maxLength or maxResults is used, there could be starts without
									routes in result. (0 - unbounded)
dests: SDName List of possible destinations. (0 - unbounded)
maxLength: int Maximum length of the resulting routes in meters. If this parameter is set, the result will not
									contain any route longer than this value. (0 - None)
maxResults: int The maximum number of results is limited to this value. Only the shortest n Routes will be returned. (0 - None)
type: CoordinateType Designated coordinate system of the resulting routes. Default is wgs84 (EPSG:4326). Default: EPSG_4326 (0 - None)
serviceType: SimpleServiceType Type of individual route (footpath or bicycle).
									* optional since version 25 Default: FOOTPATH (0 - None)
profile: IndividualProfileType Specify a certain profile to use for routing.
									* since version 25 Default: FOOT_NORMAL (0 - None)
speed: str Specify a certain driving speed for bicycle routing. Default: NORMAL (0 - None)

"""

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

"""DLRequest

Departure list request. Get a list of departures at a given time for a given station.

station: SDName The station the departures are requested for. (0 - 1)
stations: SDName  (0 - unbounded)
time: GTITime The time for the request. Including date and time. (None - None)
maxList: int The maximum number of elements the result may have. (None - None)
maxTimeOffset: int The maximum offset of a result in minutes. Default: 120 (None - 1)
allStationsInChangingNode: bool If this is set to true and the given station is a changing node with equivalent
                  stations (e.g. Wedel and S Wedel), the result would contain	departures of all equivalent
									stations. Default is true. Default: true (0 - None)
useRealtime: bool true = server is calculating a result based on realtime data. false = server only uses plan data for
									calculating result. Default: false (0 - None)
returnFilters: bool if true, a list of possible DLFilterEntries for this request will be returned. Default: false (0 - None)
filter: DLFilterEntry List of filter entries that contains lines and directions/stations. Only Departures that
                  fits to any of these filter entries will be returned. An empty list will deactivate the filter.
                  * since Version 20 (0 - unbounded)
serviceTypes: FilterServiceType A list of servicetypes to filter the result list.
                  * since version 22 (0 - unbounded)
departure: bool if false, an arrival list will be returned instead of a departure list. Default: true (0 - None)

"""

DLRequest = Schema.extend(
    BaseRequestType,
    {
        "station": SDName,
        "stations": [SDName],
        "time": GTITime,
        "maxList": int,
        "maxTimeOffset": int,
        "allStationsInChangingNode": bool,
        "useRealtime": bool,
        "returnFilters": bool,
        "filter": [DLFilterEntry],
        "serviceTypes": [FilterServiceType],
        "departure": bool,
    },
)

"""CNRequest

The check name request. The different types of requests are defined by the SDName object possible types are:
				- Type STATION
				  * name / city is set: the results are SDNames that match the name / city of the station
				  * coordinate is set: the results are stations in the vicinity (use maxDistance) of the coordinate
				- Type POI
				  * name / city is set: the results are SDNames that match the name / city of the POI
        - Type ADDRESS
				  * name / city is set: the results are SDNames that match the name / city of the address
				- Type COORDINATE
				  * coordinate is set: the result is the nearest address to the coordinate (if available)
        Type is always required.

theName: SDName SDName object with the data to check. (None - None)
maxList: int The maximum number of elements the result may have. (None - None)
maxDistance: int The maximum distance (in meters) of stations that will be returned in a search for
                  stations near to a coordinate. (0 - None)
coordinateType: CoordinateType The type of the coordinate which the server should use in the response. Default: EPSG_4326 (0 - None)
tariffDetails: bool Flag if detailed tariff information should be transferred. Default is false. Default: false (0 - None)
allowTypeSwitch: bool Flag if the server is allowed to offer results with different SDTypes
                  than in the request. Default is true. Default: true (0 - None)

"""

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

"""TariffRequestType

scheduleElements: ScheduleElementLight Requests the tariff for this schedule. Only public transport schedule elements are allowed (no
								footpathes). To reduce size of request, only id fields of stations and lines are necessary. (1 - unbounded)
departure: GTITime Date and time of first departure in scheduleElements. (None - None)
arrival: GTITime Date and time of last arrival in scheduleElements. (None - None)
returnReduced: bool Additionally returns reduced prices for online tickets.
								* since version 16 Default: false (0 - None)
returnPartialTickets: bool if value is false, the tariff informations will not contain any tickets for parts of the route. In this
								case all returned tickets are valid for the complete route. Default: true (0 - None)

"""

TariffRequestType = Schema.extend(
    BaseRequestType,
    {
        Required("scheduleElements"): All([ScheduleElementLight], Length(min=1)),
        "departure": GTITime,
        "arrival": GTITime,
        "returnReduced": bool,
        "returnPartialTickets": bool,
    },
)

"""GRRequest

The request for a route. SDName objects will be transferred.

start: SDName The SDName of the start station. (None - None)
dest: SDName The SDName of the destination station. (None - None)
via: SDName The optional SDName of the via station. Type is always STATION. (0 - None)
time: GTITime The time for the request. May be departure or arrival, depending on flag isDeparture. (None - None)
timeIsDeparture: bool Flag which defines if a time is departure or arrival. (None - None)
numberOfSchedules: int The desired number of schedules in the response. May be less. (None - None)
penalties: Penalty If no penalty is set, defaults will be used. (0 - unbounded)
tariffDetails: bool Flag if detailed tariff information should be transferred. Default is false. Default: false (0 - None)
continousSearch: bool Flag if a search is continous. Is used for later/earlier search. Default: false (0 - None)
contSearchByServiceId: ContSearchByServiceId This field contains the information to identify the service to start AFTER/BEFORE
								* since Version 29 (0 - None)
coordinateType: CoordinateType The type of the coordinate which the server should use in the response. Default: EPSG_4326 (0 - None)
schedulesBefore: int The desired number of schedules before the actual resulting route. Default: 0 (0 - None)
schedulesAfter: int The desired number of schedules after the actual resulting route. Default: 0 (0 - None)
tariffInfoSelector: TariffInfoSelector Returns Ticketinfos (in schedule) for each of this tariffs and kinds, if the given tariff and kind is
								valid on the returned schedule.
								* since version 13 (0 - unbounded)
returnReduced: bool Additionally returns reduced prices for online tickets.
								* since version 16 Default: false (0 - None)
returnPartialTickets: bool if value is false, the tariff informations will not contain any tickets for parts of the route.
								In this case all returned tickets are valid for the complete route. Default: true (0 - None)
realtime: RealtimeType Configures the consideration of realtime informations during route calculation.
								* since version 19 Default: AUTO (0 - None)
intermediateStops: bool Additionally returns all intermediate stops between start and end station.
								* since version 24 Default: false (0 - None)
useStationPosition: bool Allows the journey to start/end at stations in the neighborhood of "start"/"dest".
								* since version 27 Default: true (0 - None)
forcedStart: SDName Setting this field forces the result to start at "forcedStart", regardless of the
								"useStationPosition" flag.
								* since version 27 (0 - None)
forcedDest: SDName Setting this field forces the result to end at "forcedDest", regardless of the
								"useStationPosition" flag.
								* since version 27 (0 - None)
toStartBy: SimpleServiceType Sets the method to get to the start station. Could be either "FOOTPATH" or "BICYCLE", otherwise an
								error is returned.
								* since version 27 (0 - None)
toDestBy: SimpleServiceType Sets the method to get to the destination station. Could be either "FOOTPATH" or "BICYCLE", otherwise an
								error is returned.
								* since version 27 (0 - None)
returnContSearchData: bool returns additional cont search data
								* since version 29 (0 - None)

"""

GRRequest = Schema.extend(
    BaseRequestType,
    {
        "start": SDName,
        "dest": SDName,
        "via": SDName,
        "time": GTITime,
        "timeIsDeparture": bool,
        "numberOfSchedules": int,
        "penalties": [Penalty],
        "tariffDetails": bool,
        "continousSearch": bool,
        "contSearchByServiceId": ContSearchByServiceId,
        "coordinateType": CoordinateType,
        "schedulesBefore": int,
        "schedulesAfter": int,
        "tariffInfoSelector": [TariffInfoSelector],
        "returnReduced": bool,
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

"""ReturnCode

Enumeration with all possible return codes.
-OK: successful
-ERROR_ROUTE: server was unable to calculate route
-ERROR_COMM: communication failed
-ERROR_CN_TOO_MANY: The request information is not enough precise. More infos needed to check station.
-ERROR_TEXT: unknown error with text
-START_DEST_TOO_CLOSE: Start and destination are too close. The direct footway will be returned instead.
* Deprecated since Version 21 *
"""

ReturnCode = In(
    [
        "OK",
        "ERROR_ROUTE",
        "ERROR_COMM",
        "ERROR_CN_TOO_MANY",
        "ERROR_TEXT",
        "START_DEST_TOO_CLOSE",
    ]
)

"""ErrorType

returnCode: ReturnCode The return code of the operation. (None - None)
errorText: str User friendly textmessage that describes an error (on returnCodes != OK). (0 - None)
errorDevInfo: str additional error information for developer. This info ist not intended to be read by the user.
						* since version 15 (0 - None)

"""

ErrorType = Schema({"returnCode": ReturnCode, "errorText": str, "errorDevInfo": str})
