import requests
from models import Location, Trip
from storage import save_trip,load_trip,save_user
from weather import search_city,get_weather,WEATHER_CODES
from compare import compare_cities

User_ID=save_user(input("Please enter your name: "))
Trip_Name = input("Please enter the name of your trip: ")
Start_Date = input("Please enter the start date of your trip (YYYY-MM-DD): ")
End_Date = input("Please enter the end date of your trip (YYYY-MM-DD): ")
trip = Trip(User_ID, Trip_Name, Start_Date, End_Date)

while True:
    locations=input("Please enter the name of a city you want to visit (or type 'done' to finish): ")
    if locations=='done':
        break
    else:
        try:
            result = search_city(locations)
        except (requests.RequestException, ValueError) as e:
            print(f"Network/API error looking up '{locations}': {e}. Please try again.")
            continue
        if result is None:
            print("City not found. Please try again.")
            continue
        else:
            latitude, longitude = result
            location = Location(locations, latitude, longitude)
            print(trip.add_location(location))
            

save_trip(trip)

loaded_trip = load_trip(User_ID)

for index, loaded_t in enumerate(loaded_trip, start=1):
    print(f"{index}.")
    print(loaded_t.show_locations())

for location in trip.locations:
    weather_data = get_weather(
        location.latitude,
        location.longitude,
        trip.startdate,
        trip.enddate
    )
    if weather_data is None:                 # ① 拦住取不到数据的情况
        print(f"Weather data is not available for {location.name}. Please check the date range.")
        continue                        # 去下一个城市

    for time,weather_code,max_temp,min_temp in zip(weather_data["time"], weather_data["weather_code"], weather_data["temperature_2m_max"],weather_data["temperature_2m_min"]):   # ② 列拼成行
        description = WEATHER_CODES.get(weather_code, "Unknown")                    # ③ 码变人话
             
        print(f"City: {location.name}; Date: {time}; Weather: {description}; Max/Min: {max_temp}/{min_temp}°C")

city_names = [location.name for location in trip.locations]
if len(city_names) >= 2:
    print("\nCity comparison:")
    print(compare_cities(city_names, trip.startdate, trip.enddate))
