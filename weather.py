import requests
def search_city(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name

    }
    try:
        response = requests.get(url, params=params)
    except requests.RequestException as e:
        print(f"Error occurred while searching for city: {e}")
        return None    
    data=response.json()
    if "results" not in data:
            return None
    first_result = data["results"][0]

    latitude = first_result["latitude"]
    longitude = first_result["longitude"]

    return latitude, longitude

WEATHER_CODES = {
    0: "晴",
    1: "晴间多云",
    2: "多云",
    3: "阴",
    45: "雾",
    48: "雾凇",
    51: "小毛毛雨",
    53: "中等毛毛雨",
    55: "强毛毛雨",
    61: "小雨",
    63: "中雨",
    65: "大雨",
    71: "小雪",
    73: "中雪",
    75: "大雪",
    80: "小阵雨",
    81: "中阵雨",
    82: "强阵雨",
    95: "雷暴",
    96: "雷暴伴小冰雹",
    99: "雷暴伴强冰雹",
}

def get_weather(latitude, longitude,startdate, enddate):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": startdate,
        "end_date": enddate,
        "daily": "temperature_2m_max,temperature_2m_min,weather_code"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    daily_weather = data["daily"]
    dates = daily_weather["time"]
    max_temperatures = daily_weather["temperature_2m_max"]
    min_temperatures = daily_weather["temperature_2m_min"]
    weather_codes = daily_weather["weather_code"]
    for date, max_temp, min_temp, code in zip(
    dates,
    max_temperatures,
    min_temperatures,
    weather_codes
):
        weather = WEATHER_CODES.get(code, "未知天气")
        print(f"{date}: {weather}, 最高温: {max_temp}°C, 最低温: {min_temp}°C")
    return daily_weather




    