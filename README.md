<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9d/LogoHVV.svg" width="200" style="margin-right: 50px">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/GEOFOX-LOGO.jpg/320px-GEOFOX-LOGO.jpg" width="120">

</div>

<h2 align="center">HVV Geofox Python Library</h2>

<p align="center">
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href=""><img alt="Hamburg" src="https://img.shields.io/badge/city-hamburg-e3000f"></a>
  <a href="https://github.com/vigonotion/pygti/issues"><img alt="Open Issues" src="https://img.shields.io/github/issues/vigonotion/pygti"></a>
  <a href="https://github.com/vigonotion/pygti/releases"><img alt="Release" src="https://img.shields.io/github/release/vigonotion/pygti"></a>
  <a href="https://api-test.geofox.de/gti/doc/index.jsp"><img alt="GTI version: 38" src="https://img.shields.io/badge/gti%20version-38-green.svg"></a>
  <a href="https://dev.azure.com/vigonotion/pygti/_build/latest?definitionId=1&branchName=master"><img alt="Azure Pipelines status" src="https://dev.azure.com/vigonotion/pygti/_apis/build/status/vigonotion.pygti?branchName=master"></a>

</p>

<p><br /></p>

## About

This library is a python wrapper for accessing the geofox api. This api is used to get information about the public transport in Hamburg, Germany.

## How to get the api credentials

You have to apply for credentials via the HVV website. You can see their official guide [here](https://www.hvv.de/de/fahrplaene/abruf-fahrplaninfos/datenabruf) (the page is only available in German).

They will send you a contract you will have to sign and send back. After about a week, you will receive your api credentials.

## Documentation

This library uses the same data types and parameters as specified in the [GTI documentation](https://api-test.geofox.de/gti/doc/index.jsp). It features client side validation of the parameters.

## Installation

Install the [package from pypi](https://pypi.org/project/pygti/).

```python
pip install pygti
```

## Usage

See the examples on how to use the library at [examples.py](https://github.com/vigonotion/pygti/blob/master/examples.py), and see the [GTI documentation](https://api-test.geofox.de/gti/doc/index.jsp) for in-depth explanation of parameters.

There is also a [Glitch example](https://pygti-examples.glitch.me/) available. Try it out and if you want to see how it's done, just [remix the app](https://glitch.com/edit/#!/pygti-examples).

A minimal working example is shown below:

```python
from pygti.gti import GTI, Auth
import asyncio
import aiohttp

GTI_USER = "" # your api username
GTI_PASS = "" # your api password


async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, GTI_USER, GTI_PASS)

        gti = GTI(auth)

        ir = await gti.init()

        # see the examples.py file for more functionality and use of the payloads

asyncio.run(main())
```

> :exclamation: **If using Python 3.8**: Version 3.6.2 of aiohttp uses a different EventLoopPolicy so running this MWE will currently result in an error displayed in the console! It should not affect the functionality. This should be fixed with a newer version of aiohttp. For a workaround look into the [examples.py](https://github.com/vigonotion/pygti/blob/master/examples.py) file. For more information see this [Issue](https://github.com/aio-libs/aiohttp/issues/4324).

## Progress

- [x] 1. init
- [x] 2. checkName
- [x] 3. getRoute
- [x] 4. departureList
- [x] 5. getTariff
- [x] 6. departureCourse
- [x] 7. listStations
- [x] 8. listLines
- [x] 9. getAnnouncements
- [x] 10. getIndividualRoute
- [x] 11a. getVehicleMap
- [x] 11b. getTrackCoordinates
- [x] 12. checkPostalCode
- [x] 13. getStationInformation
- [x] 14. tariffZoneNeighbours
- [x] 15. tariffMetaData
- [x] 16. singleTicketOptimizer
- [x] 17. ticketList

## Developing

Some files in this project are generated based on the WADL and XSD schema files from GTI.
To generate them, install the dev dependencies and run the script:

```sh
pip install -r requirements_dev.txt
python script/generate.py
```

## Contributions are welcome!

If you want to contribute to this, please read the [Contribution guidelines](CONTRIBUTING.md)
