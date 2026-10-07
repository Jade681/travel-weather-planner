import requests
def search_city(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name
}

    response = requests.get(url, params=params,timeout=10)
    data=response.json()

    if "results" not in data:
            return None
    first_result = data["results"][0]

    latitude = first_result["latitude"]
    longitude = first_result["longitude"]

    return latitude, longitude

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def get_weather(latitude, longitude,startdate, enddate):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": startdate,
        "end_date": enddate,
        "daily": "temperature_2m_max,temperature_2m_min,weather_code,apparent_temperature_max,apparent_temperature_min,precipitation_probability_max,wind_speed_10m_max",
        "timezone": "auto"
    }
    try:
        response = requests.get(url, params=params,timeout=10)
        data = response.json()
    except requests.RequestException as e:
        print(f"Error occurred while fetching weather: {e}")
        return None
    except ValueError as e:
        print(f"Weather API returned non-JSON (server error?): {e}")
        return None
    if "daily" not in data:
            return None
    else:
        daily_weather = data["daily"]

    return daily_weather
