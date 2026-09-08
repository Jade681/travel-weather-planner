from models import Location, Trip
from storage import save_trip,load_trip
from weather import search_city,get_weather


city_name = input("Please enter the name of the city you want to search for: ")
result = search_city(city_name)
if result is None:
    print("City not found.")
    exit(1)
else:
    latitude, longitude = result
    city_location = Location(city_name, latitude, longitude)
    My_Trip = input("Please enter the name of your trip: ")
    Start_Date = input("Please enter the start date of your trip (YYYY-MM-DD): ")
    End_Date = input("Please enter the end date of your trip (YYYY-MM-DD): ")
    trip = Trip(My_Trip, Start_Date, End_Date)
    trip.add_location(city_location)
    trip.find_location(input("Please enter the name of the location you want to find: "))
    



    save_trip(trip)

loaded_trip = load_trip()

for index, trip in enumerate(loaded_trip, start=1):
    print(f"{index}.")
    trip.show_locations()
weather = get_weather(
    city_location.latitude,
    city_location.longitude,
    trip.startdate,
    trip.enddate
)
