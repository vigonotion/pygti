import asyncio

import aiohttp
from pygti.auth import Auth
from pygti.const import *
from pygti.gti import *

print("To run the examples, enter your credentials for the GTI API.")
gti_user = "hbtweb"
gti_pass = "vw5iX/TK{mXK"


async def main():
    async with aiohttp.ClientSession() as session:

        auth = Auth(session, gti_user, gti_pass)
        gti = GTI(auth)

        print()
        print("Example 15: tariffZoneNeighbours()")
        tzn = await gti.ticketList({"stationKey": "Master:92903"})
        print(tzn)


asyncio.run(main())
