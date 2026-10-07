# Travel Weather Planner

A Python application that helps users create travel plans and add multiple destinations. It uses SQLite to store users, trips, and locations. The application retrieves weather forecasts from Open-Meteo, rates each day as Great, Okay, or Avoid, and compares and ranks multiple cities by their weather conditions.

## Features

- Create and save travel plans for individual users
- Add multiple destinations to a trip
- Retrieve daily weather forecasts from Open-Meteo
- Rate travel days as Great, Okay, or Avoid
- Compare multiple cities in a daily table and rank them by weather suitability

## Technologies

- Python
- Object-Oriented Programming (OOP)
- SQLite
- Open-Meteo API
- Git & GitHub

## How to Run

1. Install the dependency:

   ```bash
   /opt/anaconda3/bin/python3 -m pip install -r requirements.txt
   ```

2. Start the application:

   ```bash
   /opt/anaconda3/bin/python3 main.py
   ```

The application creates its SQLite database in `data/trips.db` when it runs. City rankings use the following score: Great = 2 points, Okay = 1 point, and Avoid = 0 points.

## Known Limitation

City lookup currently uses the first result returned by the geocoding service. For ambiguous names such as `Xian`, the selected location may not be the city the user intended.
