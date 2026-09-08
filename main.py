from models import Location, Trip
from storage import save_trip,load_trip
from weather import search_city,get_weather

result = search_city("Shanghai")
if result is None:
    print("City not found.")
    exit(1)
else:
    latitude, longitude = result
    shanghai = Location("Shanghai", latitude, longitude)
    trip = Trip("My Trip","2026-09-10","2026-09-12")
    trip.add_location(shanghai)
    trip.find_location("Shanghai")
    trip.find_location("Random")


    save_trip(trip)

loaded_trip = load_trip()
for one_trip in loaded_trip:
    one_trip.show_locations()



weather = get_weather(
    shanghai.latitude,
    shanghai.longitude,
    trip.startdate,
    trip.enddate
)
