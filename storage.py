import json
from models import Trip, Location
def  location_to_dict(location):
    return {
        "name":location.name,
        "latitude": location.latitude,
        "longitude": location.longitude,
    }


def trip_to_dict(trip):
    return {
        "name": trip.name,
        "startdate": trip.startdate,
        "enddate": trip.enddate,
        "locations": [location_to_dict(location) for location in trip.locations]
    }

def save_trip(trip):
    data=trip_to_dict(trip)
    with open(f"data/trip.json", "w") as f:
        json.dump(data, f, indent=4)

def load_trip():
    try:
        with open("data/trip.json", "r") as f:
            data = json.load(f)
           
            
    except FileNotFoundError:
        print("No saved trip found.")
        return None 
    except json.JSONDecodeError:
        print("The saved trip file is corrupted.")
        return None

    trip = Trip(data["name"],
                data["startdate"],
                data["enddate"])
    for location_data in data["locations"]:
                
                location = Location(
        location_data["name"],
        location_data["latitude"],
        location_data["longitude"]
           )
                trip.locations.append(location)
    return trip