import asyncio
import os
from datetime import datetime, timedelta

import aiohttp
from pygti.auth import Auth
from pygti.gti import GTI

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
        print("Example 11: getVehicleMap()")
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
        print("Example 12: getTrackCoordinates()")
        payload = {
            "coordinateType": "EPSG_4326",
            "stopPointKeys": [
                "ZVU-DB:8004248:2",
                "ZVU-DB:8004247:2",
                "ZVU-DB:809100:1",
                "ZVU-DB:119106:1",
            ],
        }
        tc = await gti.getTrackCoordinates(payload)
        print(tc)

        print()
        print("Example 13: checkPostalCode()")
        pc = await gti.checkPostalCode({"postalCode": 20355})
        print(pc)

        print()
        print("Example 14: stationInformation()")
        si = await gti.stationInformation(
            {"station": {"name": "Wartenau", "id": "Master:10901", "type": "STATION"}}
        )
        print(si)

        print()
        print("Example 15: tariffZoneNeighbours()")
        tzn = await gti.tariffZoneNeighbours({})
        print(tzn)

        print()
        print("Example 16: ticketList()")
        tl = await gti.ticketList({"stationKey": "Master:92903"})
        print(tl)


asyncio.run(main())
