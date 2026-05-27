import asyncio
import os

import aiohttp

from pygti.auth import Auth
from pygti.gti import GTI
from pygti.models import DLRequest, GTITime, SDName, SDNameType

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]

    load_dotenv()
except ImportError:
    pass

GTI_USER = os.getenv("GTI_USER") or ""
GTI_PASS = os.getenv("GTI_PASS") or ""

if not (GTI_USER and GTI_PASS):
    print("To run the examples, enter your credentials for the GTI API.")
    GTI_USER = input("GTI Username: ")
    GTI_PASS = input("GTI Password: ")


async def main() -> None:
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

        for departure in response.departures or []:
            direction = departure.line.direction or ""
            offset = departure.timeOffset if departure.timeOffset is not None else "-"
            print(f"{departure.line.name:5} {direction:50}         {offset:>10} min")


asyncio.run(main())
