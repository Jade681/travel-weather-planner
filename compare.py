import weather


# Units: temperature in Celsius, precipitation probability in %, wind speed in km/h
def judge_day(weather_code,apparent_max,apparent_min,precip_prob,wind_max):
    if weather_code in (95,96,99,75,82) or apparent_max >= 35 or apparent_min <= -5 or precip_prob >= 80 or wind_max >= 50:
        return "Avoid"
    else:
        if apparent_max >= 32 or apparent_min <= 0 or precip_prob >= 60 or wind_max >= 38:
            return "Okay"
        else:
            return "Great"
        
  
    
def show_plan(city_name,start_date,end_date):
    latitude, longitude = weather.search_city(city_name)
    data = weather.get_weather(latitude, longitude, start_date, end_date)
    for date, weather_code, apparent_max, apparent_min, precip_prob, wind_max in zip(data["time"], data["weather_code"], data["apparent_temperature_max"], data["apparent_temperature_min"], data["precipitation_probability_max"], data["wind_speed_10m_max"]):
        print(f"City: {city_name}, Day: {date}, Verdict: {judge_day(weather_code, apparent_max, apparent_min, precip_prob, wind_max)}")
        print(f"{date}: code {weather_code}, apparent {apparent_max}/{apparent_min} °C, rain {precip_prob}%, wind {wind_max} km/h")


show_plan("Tokyo", "2026-09-18", "2026-09-22")
show_plan("Kyoto", "2026-09-23", "2026-09-27")
