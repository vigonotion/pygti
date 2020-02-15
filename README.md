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
  <a href="https://api-test.geofox.de/gti/doc/index.jsp"><img alt="GTI version: 37.4" src="https://img.shields.io/badge/gti%20version-37.4-green.svg"></a>
</p>

<p><br /></p>

## About

This library is a python wrapper for accessing the geofox api. This api is used to get information about the public transport in Hamburg, Germany.

## Documentation

This library uses the same data types and parameters as specified in the [GTI documentation](https://api-test.geofox.de/gti/doc/index.jsp). It features client side validation of the parameters.

See the examples on how to use the library at [examples.py](examples.py), and see the [GTI documentation](https://api-test.geofox.de/gti/doc/index.jsp) for parameters.

## Progress

- [x] init
- [x] checkName
- [x] getRoute
- [x] departureList
- [ ] getTariff
- [ ] departureCourse
- [ ] listStations
- [ ] listLines
- [ ] getAnnouncements
- [ ] getIndividualRoute
- [ ] getVehicleMap
- [ ] getTrackCoordinates
- [ ] checkPostalCode
- [x] getStationInformation
- [ ] tariffZoneNeighbours
- [ ] ticketList

## Tests

To run the test use the pytest module
```
$ pytest -s
```
The `-s` parameter must be used because you will be prompted to insert your api credentials and this will fail if pytest isn't silenced.
There are two groups to test: `schema` and `asyncio`. `schema` is testing your local schemas with payloads and checks if your schemas are correctly implemented. `asyncio` will send the requests to the api. Note that credentials are only used for the api call. Therefor you can use these two commands to check the parts seperatly:
```
$ pytest -m schema 
$ pytest -s -m asyncio
```  

## Contributions are welcome!

If you want to contribute to this, please read the [Contribution guidelines](CONTRIBUTING.md)
