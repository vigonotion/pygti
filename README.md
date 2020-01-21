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
- [ ] getRoute
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

## Contributions are welcome!

If you want to contribute to this, please read the [Contribution guidelines](CONTRIBUTING.md)
