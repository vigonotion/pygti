import asyncio
import os
import aiohttp

from pygti.auth import Auth
from pygti.gti import GTI
from pygti.models import DLRequest, GTITime, InitRequest, SDName, SDNameType

GTI_USER = None
GTI_PASS = None

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

GTI_USER = os.getenv("GTI_USER")
GTI_PASS = os.getenv("GTI_PASS")

if not (GTI_USER and GTI_PASS):
    print("To run the examples, enter your credentials for the GTI API.")
    GTI_USER = input("GTI Username: ")
    GTI_PASS = input("GTI Password: ")


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, GTI_USER, GTI_PASS)
        gti = GTI(auth)

        print("Example 2: departureList()")
        response = await gti.departureList(
            DLRequest(
                station=SDName(
                    name="Wartenau",
                    id="Master:10901",
                    type=SDNameType.STATION,
                ),
                time=GTITime(date="heute", time="jetzt"),
                maxList=5,
                maxTimeOffset=200,
                useRealtime=True,
            )
        )

        for departure in response.departures:
            print(
                f"{departure.line.name:5} {departure.line.direction:50}         {departure.timeOffset:>10} min"
            )


asyncio.run(main())
