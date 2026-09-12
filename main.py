from models import Location, Trip
from storage import save_trip,load_trip
from weather import search_city,get_weather

Trip_Name = input("Please enter the name of your trip: ")
Start_Date = input("Please enter the start date of your trip (YYYY-MM-DD): ")
End_Date = input("Please enter the end date of your trip (YYYY-MM-DD): ")
trip = Trip(Trip_Name, Start_Date, End_Date)

while True:
    locations=input("Please enter the name of a city you want to visit (or type 'done' to finish): ")
    if locations=='done':
        break
    else:
        result = search_city(locations)
        if result is None:
            print("City not found. Please try again.")
            continue
        else:
            latitude, longitude = result
            location = Location(locations, latitude, longitude)
            trip.add_location(location)
            

save_trip(trip)

loaded_trip = load_trip()

for index, loaded_t in enumerate(loaded_trip, start=1):
    print(f"{index}.")
    loaded_t.show_locations()

for location in trip.locations:
    weather = get_weather(
        location.latitude,
        location.longitude,
        trip.startdate,
        trip.enddate
    )
