import asyncio
import os
import sys
from datetime import datetime, timedelta

import aiohttp
from pygti.auth import Auth
from pygti.gti import GTI

GTI_USER = None
GTI_PASS = None

try:
    from dotenv import load_dotenv

    load_dotenv()

    GTI_USER = os.getenv("GTI_USER")
    GTI_PASS = os.getenv("GTI_PASS")
except ImportError:
    pass

if not (GTI_USER and GTI_PASS):
    print("To run the examples, enter your credentials for the GTI API.")
    GTI_USER = input("GTI Username: ")
    GTI_PASS = input("GTI Password: ")


async def main():
    async with aiohttp.ClientSession() as session:

        auth = Auth(session, GTI_USER, GTI_PASS)
        gti = GTI(auth)

        print("Example 1: init()")
        ir = await gti.init()
        print(ir)

        print()
        print("Example 2: checkName()")
        cn = await gti.checkName({"theName": {"name": "Wartenau"}})
        print(cn)

        print()
        print("Example 3: getRoute()")
        payload = {
            "language": "de",
            "start": {
                "name": "Ritterstraße",
                "city": "Hamburg",
                "combinedName": "Ritterstraße",
                "id": "Master:60904",
                "type": "STATION",
                "coordinate": {"x": 10.046196, "y": 53.567617},
            },
            "dest": {
                "name": "Wartenau",
                "city": "Hamburg",
                "combinedName": "Wartenau",
                "id": "Master:10901",
                "type": "STATION",
                "coordinate": {"x": 10.035515, "y": 53.56478},
            },
            "time": {"date": "heute", "time": "jetzt"},
            "timeIsDeparture": True,
            "realtime": "REALTIME",
        }
        gr = await gti.getRoute(payload)
        print(gr)

        print()
        print("Example 4.1: departureList()")
        dl = await gti.departureList(
            {
                "station": {
                    "name": "Wartenau",
                    "id": "Master:10901",
                    "type": "STATION",
                },
                "time": {"date": "heute", "time": "jetzt"},
                "maxList": 5,
                "maxTimeOffset": 200,
                "useRealtime": True,
            }
        )

        print(dl)

        print()
        print("Example 4.2: departureList(), return filters")
        dl = await gti.departureList(
            {
                "station": {
                    "name": "Wartenau",
                    "id": "Master:10901",
                    "type": "STATION",
                },
                "time": {"date": "heute", "time": "jetzt"},
                "maxList": 5,
                "maxTimeOffset": 200,
                "useRealtime": True,
                "returnFilters": True,
            }
        )
        print(dl)

        print()
        print("Example 5: getTariff()")
        gT = await gti.getTariff(
            {
                "scheduleElements": [
                    {
                        "departureStationId": "Master:10950",
                        "arrivalStationId": "Master:37979",
                        "lineId": "DB-EFZ:RE8_DB-EFZ_Z",
                    }
                ],
                "departure": {"date": "16.02.2020", "time": "8:04"},
                "arrival": {"date": "16.02.2020", "time": "8:29"},
            }
        )
        print(gT)

        print()
        print("Example 6.1: departureCourse() time and direction")
        gT = await gti.departureCourse(
            {
                "lineKey": "VHH:569_VHH",
                "station": {
                    "name": "Rosenhof",
                    "city": "Ahrensburg",
                    "combinedName": "Ahrensburg, Rosenhof",
                    "id": "Master:35009",
                    "type": "STATION",
                    "coordinate": {"x": 10.240928, "y": 53.683071},
                },
                "time": datetime.fromisoformat("2020-10-21T10:19:00.000"),
                "direction": "Ahrensburg, Schulzentrum Am Heimgarten",
            }
        )
        # print(gT)
        print(
            "departureCourse() output is too long, please uncomment only if neccessary"
        )

        # print()
        # print("Example 6.2: departureCourse() time and serviceId")
        # gT = await gti.departureCourse(
        #     {
        #         "lineKey": "HHA-U:U1_HHA-U",
        #         "station": {
        #             "name": "Wartenau",
        #             "id": "Master:10901",
        #             "type": "STATION",
        #         },
        #         "time": datetime.now(),
        #         "serviceId": 1626150555,
        #     }
        # )
        # print(gT)
        print(
            "departureCourse() output is too long, please uncomment only if neccessary"
        )

        print("Example 7: listStations()")
        # used a older dataReleaseID to show changes since then in the response
        ls = await gti.listStations({"dataReleaseID": "32.17.02"})
        print(ls)

        print()
        print("Example 8: listLines()")
        ll = await gti.listLines({"dataReleaseID": "32.17.02"})
        print(ll)

        print("Example 9: AnnouncementRequest")
        ar = await gti.getAnnouncements(
            {
                "names": ["S3"],
                "timeRange": {
                    "begin": datetime.now() - timedelta(days=2),
                    "end": datetime.now() + timedelta(days=10),
                },
            }
        )

        print(ar)

        print()
        print("Example 10: getIndividualRoute()")
        payload = {
            "starts": [
                {"type": "ADDRESS", "coordinate": {"x": 9.92496, "y": 53.563494}}
            ],
            "dests": [
                {"type": "ADDRESS", "coordinate": {"x": 9.924269, "y": 53.562925}}
            ],
            "maxLength": 10000,
            "serviceType": "BICYCLE",
            "profile": "BICYCLE_NORMAL",
            "speed": "NORMAL",
        }
        indRoute = await gti.getIndividualRoute(payload)
        print(indRoute)

        print()
        print("Example 11a: getVehicleMap()")
        payload = {
            "boundingBox": {
                "lowerLeft": {"x": 9.985707, "y": 53.573138, "type": "EPSG_4326"},
                "upperRight": {"x": 9.992702, "y": 53.576916, "type": "EPSG_4326"},
            },
            "periodBegin": int(datetime.timestamp(datetime.now())),
            "periodEnd": int(datetime.timestamp(datetime.now() + timedelta(minutes=1))),
            "withoutCoords": True,
            "coordinateType": "EPSG_31467",
            "vehicleTypes": ["U_BAHN"],
            "realtime": False,
        }
        vm = await gti.getVehicleMap(payload)
        print(vm)

        print()
        print("Example 11b: getTrackCoordinates()")
        payload = {
            "coordinateType": "EPSG_4326",
            "stopPointKeys": ["HHA-U:909010:1", "HHA-U:119000:1"],
        }
        tc = await gti.getTrackCoordinates(payload)
        print(tc)

        print()
        print("Example 12: checkPostalCode()")
        pc = await gti.checkPostalCode({"postalCode": 20355})
        print(pc)

        print()
        print("Example 13: stationInformation()")
        si = await gti.stationInformation(
            {"station": {"name": "Wartenau", "id": "Master:10901", "type": "STATION"}}
        )
        print(si)

        print()
        print("Example 14: tariffZoneNeighbours()")
        tzn = await gti.tariffZoneNeighbours({})
        print(tzn)

        print()
        print("Example 15.1: tariffMetaData() in german")
        tmd = await gti.tariffMetaData({})
        print(tmd)

        print()
        print("Example 15.2: tariffMetaData() in english")
        tmd = await gti.tariffMetaData({"language": "en"})
        print(tmd)

        print()
        print("Example 16.1: singleTicketOptimizer()")
        sto = await gti.singleTicketOptimizer(
            {
                "withReturnJourney": True,
                "numberOfAdults": 2,
                "numberOfChildren": 0,
                "tickets": [],
                "route": {
                    "trip": [
                        {
                            "start": {"id": "Master:43063", "name": "Außenmühle"},
                            "destination": {
                                "id": "Master:49001",
                                "name": "Bf. Harburg",
                            },
                            "line": {"id": "HHA-B:145_HHA-B", "name": "145"},
                            "vehicleType": "Bus",
                        },
                        {
                            "start": {"id": "Master:49950", "name": "Harburg"},
                            "destination": {
                                "id": "Master:80950",
                                "name": "Landungsbrücken",
                            },
                            "line": {"id": "SBH:S3_SBH_SBAHNS", "name": "S3"},
                            "vehicleType": "S",
                        },
                        {
                            "start": {
                                "id": "Master:80984",
                                "name": "Landungsbrücken Brücke 1",
                            },
                            "destination": {
                                "id": "Master:80932",
                                "name": "Elbphilharmonie",
                            },
                            "line": {"id": "ZVU-DB:72_ZVU-DB_HADAGZ", "name": "72"},
                            "vehicleType": "Schiff",
                        },
                    ],
                    "departure": datetime.fromisoformat("2020-04-17T18:16:00.000"),
                    "arrival": datetime.fromisoformat("2020-04-17T19:14:00.000"),
                    "tariffRegions": {
                        "zones": [{"regions": ["308", "208", "108", "000"]}],
                        "rings": [{"regions": ["B", "A"]}],
                        "counties": [{"regions": ["HH1", "HH2"]}],
                    },
                    "singleTicketTariffLevelId": 14,
                    "extraFareType": "NO",
                },
            }
        )
        print(sto)

        print()
        print("Example 17: ticketList()")
        tl = await gti.ticketList({"stationKey": "Master:92903"})
        print(tl)


# To avoid 'Event loop is closed' RuntimeError due to compatibility issue with aiohttp
if sys.platform.startswith("win") and sys.version_info >= (3, 8):
    try:
        from asyncio import WindowsSelectorEventLoopPolicy
    except ImportError:
        pass
    else:
        if not isinstance(
            asyncio.get_event_loop_policy(), WindowsSelectorEventLoopPolicy
        ):
            asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
asyncio.run(main())
