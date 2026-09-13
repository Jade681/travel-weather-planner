import storage
from models import Location, Trip

storage.cursor.execute("PRAGMA table_info(trips)")
print(storage.cursor.fetchall())

storage.cursor.execute("PRAGMA table_info(users)")
print(storage.cursor.fetchall())

my_trip = Trip(1,"test trip", "2026-09-20", "2026-09-25")
location1=Location("New York", 40.7128, -74.0060)

my_trip.add_location(location1)
storage.save_trip(my_trip)
loaded_trips = storage.load_trip()
for t in loaded_trips:
    print(t.userid)
    t.show_locations()