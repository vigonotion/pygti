import asyncio
import os
import aiohttp

from pygti.auth import Auth
from pygti.gti import GTI
from pygti.models import InitRequest

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

        print("Example 1: init()")
        ir = await gti.init(InitRequest())
        print(ir)


asyncio.run(main())
