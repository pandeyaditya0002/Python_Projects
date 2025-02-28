import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your actual API key
    base_url = "https://api.weatherapi.com/v1/current.json"
    
    if api_key == "your_api_key_here" or not api_key:
        return {"Error": "Invalid API key. Please replace it with a valid one."}
    
    params = {"key": api_key, "q": city, "aqi": "no"}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if "current" in data:
            weather = {
                "City": data["location"]["name"],
                "Region": data["location"]["region"],
                "Country": data["location"]["country"],
                "Temperature": f"{data['current']['temp_c']}°C",
                "Feels Like": f"{data['current']['feelslike_c']}°C",
                "Humidity": f"{data['current']['humidity']}%",
                "Pressure": f"{data['current']['pressure_mb']} hPa",
                "Wind Speed": f"{data['current']['wind_kph']} km/h",
                "Weather": data["current"]["condition"]["text"]
            }
            return weather
        else:
            return {"Error": "Unexpected response format."}
    except requests.exceptions.HTTPError as http_err:
        return {"Error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"Error": f"Request error occurred: {req_err}"}

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

'''
url = f"https://api.weatherapi.com/v1/current.json?q={zip_code}&lang=en&key=6c287fa0ee684ae9a2e150557252502"
    headers = {"accept": "application/json"}
'''