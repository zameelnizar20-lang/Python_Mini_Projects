import requests  # 1: import the library we use to make HTTP requests

# 2: get user input (the city name)
city = input("Enter city name: ").strip()

# 3: your API key (string) — get it from OpenWeatherMap after signup
api_key = "962b46112bcecb9c02b296eb9f3c26b7"

# 4: base URL for OpenWeatherMap current weather endpoint
base_url = "https://api.openweathermap.org/data/2.5/weather"

# 5: build the parameters dictionary (preferred over string-concatenation)
params = {
    "q": city,           # city name to search
    "appid": api_key,    # your API key for authentication
    "units": "metric"    # returns temperatures in Celsius; use "imperial" for °F
}

# 6: send GET request inside try-except to catch network errors
try:
    response = requests.get(base_url, params=params, timeout=10)
except requests.RequestException as e:
    # network-level problem (DNS, connection, timeout, etc.)
    print("Network error:", e)
    raise SystemExit  # stop the program

# 7: check HTTP status code to decide next steps
if response.status_code == 200:
    # 8: convert JSON text into Python dict
    data = response.json()

    # 9: defensive access — make sure expected keys exist
    main = data.get("main", {})
    weather_list = data.get("weather", [])
    weather = weather_list[0] if weather_list else {}

    temperature = main.get("temp")
    feels_like = main.get("feels_like")
    humidity = main.get("humidity")
    condition = weather.get("description")

    # 10: pretty print results (handle None values gracefully)
    print(f"🌤️ Weather in {city.title()}:")
    print(f"Temperature: {temperature if temperature is not None else 'N/A'}°C")
    print(f"Feels like: {feels_like if feels_like is not None else 'N/A'}°C")
    print(f"Condition: {condition if condition else 'N/A'}")
    print(f"Humidity: {humidity if humidity is not None else 'N/A'}%")

elif response.status_code == 401:
    print("❌ Unauthorized: check your API key (invalid or missing).")
elif response.status_code == 404:
    print("❌ City not found. Check the city name spelling.")
else:
    # generic fallback — show status code and message for debugging
    print(f"❌ Error {response.status_code}: {response.text}")


