from pygti.gti import *

print("To run the examples, enter your credentials for the GTI API.")
gti_user = input("GTI Username: ")
gti_pass = input("GTI Password: ")

gti = GTI(gti_user, gti_pass)

print("Example 1: init()")
ir = gti.init()
print(ir)

print()
print("Example 2: checkName()")
cn = gti.checkName({"theName": {"name": "Wartenau"}})
print(cn)

print()
print("Example 3.1: departureList()")
dl = gti.departureList(
    {
        "station": {"name": "Wartenau", "id": "Master:10901", "type": "STATION"},
        "time": {"date": "heute", "time": "jetzt"},
        "maxList": 5,
        "maxTimeOffset": 200,
        "useRealtime": True,
    }
)

print(dl)

print()
print("Example 3.2: departureList(), only trains")
dl = gti.departureList(
    {
        "station": {"name": "Wartenau", "id": "Master:10901", "type": "STATION"},
        "time": {"date": "heute", "time": "jetzt"},
        "maxList": 5,
        "maxTimeOffset": 200,
        "useRealtime": True,
        "returnFilters": True,
    }
)

print(dl)
