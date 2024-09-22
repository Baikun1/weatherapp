import requests

BASE_URL = 'https://freetestapi.com/api/v1/weathers'

def get_weather(city):
    # Build the complete API URL
    url = f"{BASE_URL}?search={city}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON response
        data = response.json()
        
        # Check if the city was found
        if not data:
            print("Error: City not found.")
            return
        
        # Extract and display the relevant information
        weather_info = data[0]  # Get the first result
        city_name = weather_info['city']
        country = weather_info['country']
        temperature = weather_info['temperature']
        humidity = weather_info['humidity']
        wind_speed = weather_info['wind_speed']
        weather_description = weather_info['weather_description']
        
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {weather_description.capitalize()}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
