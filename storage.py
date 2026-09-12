import sqlite3
from models import Trip, Location

conn = sqlite3.connect("data/trips.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY,
        name TEXT,
        startdate TEXT,
        enddate TEXT
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY,
        trip_id INTEGER,
        name TEXT,
        latitude REAL,
        longitude REAL,
        FOREIGN KEY (trip_id) REFERENCES trips(id)
    )
""")
    
def save_trip(trip):    
    cursor.execute("INSERT INTO trips (name, startdate, enddate) VALUES (?, ?, ?)", (trip.name, trip.startdate, trip.enddate))
    trip_id = cursor.lastrowid

    for location in trip.locations:
        cursor.execute("INSERT INTO locations (trip_id, name,latitude, longitude) VALUES (?,?,?,?)",
                    (trip_id,location.name,location.latitude,location.longitude))

    conn.commit()
   
def load_trip():
    all_trips = []

    cursor.execute("SELECT * FROM trips")
    trip_rows = cursor.fetchall()

    for trip_row in trip_rows:
        # trip_row 长这样：(id, name, startdate, enddate)
        trip = Trip(trip_row[1], trip_row[2], trip_row[3])   # 取出 name, startdate, enddate
        this_trip_id = trip_row[0]                            # 取出 id，等下查它的地点要用

        cursor.execute("SELECT * FROM locations WHERE trip_id = ?", (this_trip_id,))
        location_rows = cursor.fetchall()

        for location_row in location_rows:
            # location_row 长这样：(id, trip_id, name, latitude, longitude)
            location = Location(location_row[2], location_row[3], location_row[4])   # 你来填：取出 name, latitude, longitude
            trip.locations.append(location)

        all_trips.append(trip)

    return all_trips   