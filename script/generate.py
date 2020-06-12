"""Generate library files based on the GTI WADL/XSD."""

import asyncio

import aiohttp
from xsd_to_vol import xsd_to_vol


async def generate():
    async with aiohttp.ClientSession() as session:
        url = "https://api-prod.geofox.de/gti/public/geofoxThinInterfacePublic.xsd"
        async with session.get(url) as resp:
            if resp.status == 200:
                xsd = await resp.read()

                with open("pygti/schemas.py", "w") as vol_file:
                    vol_file.write(xsd_to_vol(xsd))


asyncio.run(generate())
