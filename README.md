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

See the examples on how to use the library at [examples.py](examples.py), and see the [GTI documentation](https://api-test.geofox.de/gti/doc/index.jsp) for parameters.

## Progress

- [x] 1. init
- [x] 2. checkName
- [x] 3. getRoute
- [x] 4. departureList
- [x] 5. getTariff
- [ ] ~~6. departureCourse~~ *
- [x] 7. listStations
- [x] 8. listLines
- [x] 9. getAnnouncements
- [x] 10. getIndividualRoute
- [x] 11. getVehicleMap
- [X] 12. getTrackCoordinates
- [x] 13. checkPostalCode
- [x] 14. getStationInformation
- [x] 15. tariffZoneNeighbours
- [x] 16. ticketList

\* departureCourse seems to be broken. Also, we were not able to "guess" the correct usage and it's not used on the official HVV page. If you find a solution to this, please open a PR.

## Contributions are welcome!

If you want to contribute to this, please read the [Contribution guidelines](CONTRIBUTING.md)
