# Migration Guide: → V1

This guide covers all breaking changes between the pre-V1 releases and V1. V1 introduces typed Pydantic models for all requests and responses, a simplified authentication interface, and a minimum Python version of 3.12.

---

## Summary: What you need to do

1. Upgrade to Python 3.12+
2. Add `pydantic` as a dependency
3. Replace `HMACAuth`/`AuthStrategy`/`NoAuth` → `Auth`
4. Replace `AiohttpRequest` → removed (session is now part of `Auth`)
5. Change `GTI(auth, request)` → `GTI(auth, language="de")`
6. Replace `from pygti.schemas import ...` → `from pygti.models import ...`
7. Replace `from pygti.exceptions import ...` → `from pygti.auth import GTIError`
8. Replace all `dict` payloads with typed Pydantic model instances
9. Replace `result["key"]` dict access with `result.key` attribute access
10. Add `InitRequest()` argument to `gti.init()`
11. Rename: `stationInformation` → `getStationInformation`
12. Rename: `getVehicleMap` → `getVehicleMapPublic`
13. Rename: `getTrackCoordinates` → `getTrackCoordinatesPublic`
14. Rename: `TariffRequestType` → `TariffRequest`
15. Update exception handling to use `GTIError` with `e.return_code`
16. Make `datetime` objects timezone-aware in `DCRequest.time` and `AnnouncementRequest.timeRange`

---

## Breaking changes in detail

### 1. Python version

**Before:** `>=3.6.0`  
**After:** `>=3.12`

### 2. New dependency: pydantic

V1 uses Pydantic v2 for all request and response models. Add it to your dependencies:

```sh
pip install pydantic
```

### 3. Auth interface

**Before:**
```python
from pygti.auth import HMACAuth, AuthStrategy, NoAuth

auth = HMACAuth(username, password)
```

**After:**
```python
from pygti.auth import Auth

auth = Auth(session, username, password)
# Optional: custom host (e.g. test environment)
auth = Auth(session, username, password, host="api-test.geofox.de")
```

The aiohttp `ClientSession` is now passed to `Auth` directly. `HMACAuth`, `AuthStrategy`, and `NoAuth` are removed.

### 4. GTI constructor

**Before:**
```python
from pygti.request import AiohttpRequest

request = AiohttpRequest(session)
gti = GTI(auth, request)
```

**After:**
```python
gti = GTI(auth)
# Optional: set response language globally
gti = GTI(auth, language="en")
```

`AiohttpRequest` and the entire `pygti.request` module are removed. Per-call language overrides are no longer supported; set `language` once in the `GTI` constructor.

### 5. Import paths

| Before | After |
|---|---|
| `from pygti.auth import HMACAuth, AuthStrategy, NoAuth` | `from pygti.auth import Auth` |
| `from pygti.schemas import CNRequest, DLRequest, ...` | `from pygti.models import CNRequest, DLRequest, ...` |
| `from pygti.exceptions import GTIError, CannotConnect, ...` | `from pygti.auth import GTIError` |
| `from pygti.request import AiohttpRequest` | *(removed)* |

### 6. Dict payloads → Pydantic models

All GTI methods now require typed Pydantic model instances instead of plain dicts.

**Before:**
```python
result = await gti.departureList({
    "station": {"name": "Wartenau", "id": "Master:10901", "type": "STATION"},
    "time": {"date": "heute", "time": "jetzt"},
    "maxList": 5,
})
```

**After:**
```python
from pygti.models import DLRequest, SDName, SDNameType, GTITime

result = await gti.departureList(
    DLRequest(
        station=SDName(name="Wartenau", id="Master:10901", type=SDNameType.STATION),
        time=GTITime(date="heute", time="jetzt"),
        maxList=5,
    )
)
```

### 7. Dict response → Pydantic model

**Before:**
```python
result = await gti.departureList(...)
name = result["departures"][0]["line"]["name"]  # dict access
```

**After:**
```python
result = await gti.departureList(...)
name = result.departures[0].line.name  # attribute access
```

All responses are now validated, typed Pydantic objects.

### 8. `gti.init()` requires an argument

**Before:**
```python
ir = await gti.init()
```

**After:**
```python
from pygti.models import InitRequest

ir = await gti.init(InitRequest())
```

### 9. Renamed methods

| Before | After |
|---|---|
| `gti.stationInformation(payload)` | `gti.getStationInformation(payload)` |
| `gti.getVehicleMap(payload)` | `gti.getVehicleMapPublic(payload)` |
| `gti.getTrackCoordinates(payload)` | `gti.getTrackCoordinatesPublic(payload)` |

### 10. Renamed model: `TariffRequestType` → `TariffRequest`

**Before:**
```python
from pygti.schemas import TariffRequestType
```

**After:**
```python
from pygti.models import TariffRequest
```

### 11. `SDType` string → `SDNameType` enum

**Before:**
```python
{"type": "STATION"}
```

**After:**
```python
from pygti.models import SDNameType

SDName(type=SDNameType.STATION)
```

New values in V1: `SDNameType.BIKE_AND_RIDE`, `SDNameType.STOP_POINT`.

### 12. Timezone-aware datetimes

`DCRequest.time` and `AnnouncementRequest.timeRange.begin`/`.end` now require timezone-aware `datetime` objects (`AwareDatetime`). Naive datetimes will be rejected by Pydantic.

**Before:**
```python
from datetime import datetime

DCRequest(..., time=datetime.fromisoformat("2024-01-15T10:00:00"))
```

**After:**
```python
from datetime import datetime, timezone

DCRequest(..., time=datetime(2024, 1, 15, 10, 0, 0, tzinfo=timezone.utc))
```

### 13. `language` and `version` per request removed

**Before:**
```python
await gti.tariffMetaData({"language": "en"})
```

**After:** Set `language` once at the `GTI` constructor. The protocol version is always `63` and cannot be overridden.

```python
gti = GTI(auth, language="en")
await gti.tariffMetaData(TariffMetaDataRequest())
```

### 14. Exception handling

Specialized exceptions (`CannotConnect`, `InvalidAuth`, `CheckNameTooMany`, `CommunicationError`, `RouteError`) are removed. All API errors are raised as `GTIError`.

**Before:**
```python
from pygti.exceptions import CheckNameTooMany, CannotConnect

try:
    await gti.checkName(...)
except CheckNameTooMany:
    ...
except CannotConnect:
    ...
```

**After:**
```python
from pygti.auth import GTIError

try:
    await gti.checkName(...)
except GTIError as e:
    if e.return_code == "ERROR_CN_TOO_MANY":
        ...
    print(e.error_text, e.error_dev_info)
```
