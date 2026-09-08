import sqlite3

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
conn.commit()

cursor.execute("INSERT INTO trips (name, startdate, enddate) VALUES (?, ?, ?)", ("My Trip", "2026-09-10", "2026-09-12"))

cursor.execute("SELECT * FROM trips")
rows = cursor.fetchall()
print(rows)