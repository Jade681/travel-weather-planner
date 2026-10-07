import weather
import requests

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
    try:
        coords = weather.search_city(city_name)
    except (requests.RequestException, ValueError) as e:
        print(f"Network/API error looking up '{city_name}': {e}")
        return []
    if coords is None:
        print(f"City not found: {city_name}")
        return []
    latitude, longitude = coords
    data = weather.get_weather(latitude, longitude, start_date, end_date)
    if data is None:
        return []
    plan=[]
    for date, weather_code, apparent_max, apparent_min, precip_prob, wind_max in zip(data["time"], data["weather_code"], data["apparent_temperature_max"], data["apparent_temperature_min"], data["precipitation_probability_max"], data["wind_speed_10m_max"]):
        verdict = judge_day(weather_code, apparent_max, apparent_min, precip_prob, wind_max)
        plan.append((date, verdict))
    return plan


def count_verdicts(plan):
    counts = {"Great": 0, "Okay": 0, "Avoid": 0}
    for _, verdict in plan:
        counts[verdict] += 1
    return counts

def compare_cities(cities, start_date, end_date):
    if not cities:
        return "Unable to compare: no cities were provided."

    city_plans = {}
    for city in cities:
        plan = show_plan(city, start_date, end_date)
        if not plan:
            return f"Unable to compare: no weather plan for {city}."
        city_plans[city] = plan

    lines = []
    lines.append(" | ".join(["Date"] + cities))

    first_city = cities[0]
    reference_plan = city_plans[first_city]
    for day_index in range(len(reference_plan)):
        date = reference_plan[day_index][0]
        row = [date]
        for city in cities:
            verdict = city_plans[city][day_index][1]
            row.append(verdict)
        verdicts = row[1:]
        is_different = len(set(verdicts)) > 1
        row_line = " | ".join(row)
        if is_different:
            row_line += " | Different"
        lines.append(row_line)

    lines.append("-" * 40)

    scores = {}
    for city in cities:
        counts = count_verdicts(city_plans[city])
        lines.append(
            f"{city}: Great={counts['Great']}, Okay={counts['Okay']}, Avoid={counts['Avoid']}"
        )
        scores[city] = counts["Great"] * 2 + counts["Okay"]

    ranking = sorted(cities, key=lambda city: scores[city], reverse=True)
    ranking_text = ", ".join(
        f"{position}. {city} ({scores[city]} points)"
        for position, city in enumerate(ranking, start=1)
    )
    lines.append(f"Ranking: {ranking_text}")

    best_score = scores[ranking[0]]
    best_cities = [city for city in ranking if scores[city] == best_score]
    if len(best_cities) == 1:
        lines.append(f"Recommendation: {best_cities[0]} has the best weather outlook.")
    else:
        lines.append(f"Recommendation: Tie between {', '.join(best_cities)}.")

    return "\n".join(lines)
