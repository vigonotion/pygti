# Migration Guide: 0.10.x → 1.0

## Overview

Version 1.0 is a significant rewrite. The main changes are:

- **Typed request and response models** (Pydantic v2) replace plain dicts and `voluptuous` schemas
- **Methods return typed objects** instead of raw dicts
- **Exception hierarchy simplified** — all API errors raise `GTIError`
- **Some methods renamed** to match the upstream API
- **`init()` now requires an argument**

---

## 1. Request payloads: dicts → Pydantic models

Previously, you passed plain dicts to every method. Now you pass a typed model instance imported from `pygti.models`.

**Before:**
```python
from pygti.gti import GTI

response = await gti.departureList({
    "station": {"name": "Wartenau", "id": "Master:10901", "type": "STATION"},
    "time": {"date": "heute", "time": "jetzt"},
    "maxList": 5,
})
```

**After:**
```python
from pygti.gti import GTI
from pygti.models import DLRequest, GTITime, SDName, SDNameType

response = await gti.departureList(
    DLRequest(
        station=SDName(name="Wartenau", id="Master:10901", type=SDNameType.STATION),
        time=GTITime(date="heute", time="jetzt"),
        maxList=5,
    )
)
```

The model names follow the pattern `<MethodAbbreviation>Request` (e.g. `DLRequest` for `departureList`, `GRRequest` for `getRoute`, `CNRequest` for `checkName`). All models are available in `pygti.models`.

---

## 2. Responses: raw dicts → typed models

Methods now return typed Pydantic model instances instead of `await response.json()`.

**Before:**
```python
result = await gti.departureList(payload)
# result is a plain dict
departures = result.get("departures", [])
for d in departures:
    print(d["line"]["name"])
```

**After:**
```python
result = await gti.departureList(payload)
# result is a DLResponse instance
for departure in result.departures or []:
    print(departure.line.name)
```

Optional fields are typed as `T | None`, so guard against `None` where needed.

---

## 3. Exception handling simplified

The specialized exception subclasses (`CannotConnect`, `InvalidAuth`, `CheckNameTooMany`, `CommunicationError`, `RouteError`) are gone. All API errors now raise `GTIError`.

**Before:**
```python
from pygti.exceptions import GTIError, InvalidAuth, CannotConnect

try:
    result = await gti.checkName(payload)
except InvalidAuth:
    ...
except CannotConnect:
    ...
```

**After:**
```python
from pygti.exceptions import GTIError

try:
    result = await gti.checkName(payload)
except GTIError as e:
    print(e.return_code)   # e.g. "ERROR_TEXT", "ERROR_CN_TOO_MANY"
    print(e.error_text)
```

Check `e.return_code` against the `ReturnCode` enum in `pygti.models` to distinguish error types.

---

## 4. Renamed methods

| 0.10.x | 1.0 |
|---|---|
| `stationInformation()` | `getStationInformation()` |
| `getVehicleMap()` | `getVehicleMapPublic()` |
| `getTrackCoordinates()` | `getTrackCoordinatesPublic()` |

---

## 5. `init()` now requires an argument

`init()` previously took no arguments. It now requires an `InitRequest` instance (which can be empty).

**Before:**
```python
result = await gti.init()
```

**After:**
```python
from pygti.models import InitRequest

result = await gti.init(InitRequest())
```

---

## 6. Optional: language parameter on `GTI`

The `GTI` constructor now accepts an optional `language` parameter (default `"de"`). Previously language was hardcoded per request.

```python
gti = GTI(auth, language="en")
```
