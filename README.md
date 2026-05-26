<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9d/LogoHVV.svg" width="200" style="margin-right: 50px">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/GEOFOX-LOGO.jpg/320px-GEOFOX-LOGO.jpg" width="120">

</div>

<h2 align="center">HVV Geofox Python Library</h2>

<p align="center">
  <a href="https://github.com/vigonotion/pygti/releases"><img alt="Release" src="https://img.shields.io/github/release/vigonotion/pygti"></a>
</p>

<p><br /></p>

## About

This library is a Python wrapper for the Geofox API, which provides public transport data for Hamburg, Germany (HVV). It uses `aiohttp` for async HTTP requests and returns fully typed Pydantic models for all responses.

## How to get API credentials

Apply for credentials via the HVV website. See their official guide [here](https://www.hvv.de/de/fahrplaene/abruf-fahrplaninfos/datenabruf) (German only). After signing and returning the contract, you will receive your credentials within about a week.

## Documentation

This library mirrors the data types and parameters defined in the [GTI documentation](https://gti.geofox.de/). All request and response types are Pydantic models generated from the GTI OpenAPI spec.

## Installation

Install from [PyPI](https://pypi.org/project/pygti/):

```sh
pip install pygti
```

**Requirements:** Python 3.12+, `aiohttp`, `pydantic`

## Usage

### Minimal example

```python
import asyncio
import aiohttp
from pygti.auth import Auth
from pygti.gti import GTI
from pygti.models import InitRequest

async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "GTI_USERNAME", "GTI_PASSWORD")
        gti = GTI(auth)

        ir = await gti.init(InitRequest())
        print(ir.version, ir.buildDate)

asyncio.run(main())
```

### Departure list

```python
import asyncio
import aiohttp
from pygti.auth import Auth
from pygti.gti import GTI
from pygti.models import DLRequest, GTITime, SDName, SDNameType

async def main():
    async with aiohttp.ClientSession() as session:
        auth = Auth(session, "GTI_USERNAME", "GTI_PASSWORD")
        gti = GTI(auth)

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

        for dep in response.departures:
            print(f"{dep.line.name:5} -> {dep.line.direction}  in {dep.timeOffset} min")

asyncio.run(main())
```

### Connection search

```python
from pygti.models import GRRequest, SDName, SDNameType, GTITime

response = await gti.getRoute(
    GRRequest(
        start=SDName(name="Hamburg Hbf", type=SDNameType.STATION),
        dest=SDName(name="Hamburg Airport", type=SDNameType.STATION),
        time=GTITime(date="heute", time="jetzt"),
    )
)

for schedule in response.schedules:
    print(schedule.plannedDepartureTime, "->", schedule.plannedArrivalTime)
```

### Error handling

```python
from pygti.auth import GTIError

try:
    response = await gti.departureList(...)
except GTIError as e:
    print(f"API error: {e.return_code} — {e.error_text}")
```

### Options

```python
# Custom host (e.g. test environment)
auth = Auth(session, username, password, host="api-test.geofox.de")

# English responses
gti = GTI(auth, language="en")
```

## API reference

All methods on `GTI` are async and accept a typed request model, returning a typed response model.

All request and response models are importable from `pygti.models`. See the [GTI documentation](https://gti.geofox.de/) for detailed parameter descriptions.

## Migrating from a pre-V1 version

See [MIGRATION_TO_V1.md](MIGRATION_TO_V1.md) for a full list of breaking changes and how to update your code.

## Developing

The models in `pygti/models.py` are generated from the GTI OpenAPI spec. To regenerate them:

```sh
pip install -e ".[dev]"
python scripts/codegen.py
```

## Contributions are welcome!

If you want to contribute, please read the [Contribution guidelines](CONTRIBUTING.md).
