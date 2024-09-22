
# Weather App Description

## Overview
This Python weather application fetches real-time weather data for a specified city using the FreeTestAPI. It prompts the user for a city name, retrieves weather information, and displays it in a user-friendly format.

## Code Components

1. **Imports**
   - The code imports the `requests` library, which is used to make HTTP requests to the API.

2. **Base URL**
   - The `BASE_URL` variable contains the endpoint for the FreeTestAPI weather data:
     ```python
     BASE_URL = 'https://freetestapi.com/api/v1/weathers'
     ```

3. **Function: `get_weather(city)`**
   - This function takes a city name as input and performs the following steps:
     - Constructs the complete API URL with the city name as a query parameter.
     - Sends a GET request to the API.
     - Checks for errors in the response and raises exceptions for HTTP errors.
     - Parses the JSON response to extract relevant weather information.
     - Displays:
       - City name and country
       - Temperature (in °C)
       - Humidity (in %)
       - Wind speed (in m/s)
       - Weather description

4. **Main Execution Block**
   - The code checks if it is being run as the main program:
     ```python
     if __name__ == "__main__":
     ```
   - It prompts the user to enter a city name and calls the `get_weather` function to display the weather information.

## Error Handling

 - The application includes basic error handling to manage HTTP errors and cases where a city is not found. If the API response does not return any data, an appropriate error message is 
 displayed.

## Example Output

When the user runs the program and inputs a city name, they receive output similar to the following:
```plaintext
Enter city name: London
Weather in London, GB:
Temperature: 15°C
Humidity: 82%
Wind Speed: 5.0 m/s
Description: Clear sky
```


### Requirements
The application requires the requests library. You can install it using pip:
```bash
Copy code
pip install requests
Conclusion
This weather app is a simple yet effective way to retrieve and display weather information using an external API. It can be further enhanced by adding features such as a graphical user interface (GUI), extended forecasts, or support for multiple cities.
