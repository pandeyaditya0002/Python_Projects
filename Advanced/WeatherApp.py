
import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Feels Like": f"{data['main']['feels_like']}°C",
            "Min Temperature": f"{data['main']['temp_min']}°C",
            "Max Temperature": f"{data['main']['temp_max']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Pressure": f"{data['main']['pressure']} hPa",
            "Wind Speed": f"{data['wind']['speed']} m/s",
            "Weather": data["weather"][0]["description"].capitalize()
        }
        return weather
    else:
        return {"Error": data.get("message", "Unable to fetch weather")}

def main():
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye!")
            break
        weather = get_weather(city)
        for key, value in weather.items():
            print(f"{key}: {value}")
        print("-" * 40)

if __name__ == "__main__":
    main()