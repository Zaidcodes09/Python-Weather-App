# Python Weather App 🌤️

## Description

This project is a Python-based weather application that uses the **OpenWeather API** to retrieve and display real-time weather information for any city.

The user enters a city name, and the program sends an API request to OpenWeather. The returned JSON data is processed and displayed as a formatted weather report containing temperature, humidity, weather conditions, and wind speed.

This project demonstrates API integration, JSON data handling, Python functions, and modular programming.

## Features

- Retrieves live weather data using the OpenWeather API
- Allows users to search weather by city name
- Displays:
  - City name
  - Current temperature
  - Feels-like temperature
  - Humidity
  - Weather description
  - Wind speed
- Handles invalid city searches
- Uses separate Python files for better organization

## Technologies Used

- Python 3
- Requests Library
- OpenWeather API
- JSON Data Processing

## Project Structure

```
Python-Weather-App/
│
├── main.py          # Main program that handles user input and displays weather
├── weather.py       # Handles API requests and retrieves weather data
├── README.md        # Project documentation
└── LICENSE          # MIT License
```

## Setup Instructions

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Install Required Library

Install the requests library:

```bash
pip install requests
```

### 3. Create an OpenWeather API Key

This project requires an API key from OpenWeather.

Steps:

1. Visit:
https://openweathermap.org/

2. Create an account.

3. Go to your API keys section.

4. Generate a new API key.

5. Create a file called:

```
config.py
```

6. Add your API key:

```python
API_KEY = "your_api_key_here"
```

Replace `"your_api_key_here"` with your actual API key.

**Do not share your API key publicly.**

## How to Run

Run the program using:

```bash
python main.py
```

Enter a city name when prompted, and the program will display the current weather information.

## Example Output

```
-----Weather Report-----

City: Waterloo
Temperature: 22°C
Feels Like: 21°C
Humidity: 60%
Weather: Clear Sky
Wind Speed: 5 kph

----------------------------
```

## How It Works

1. The user enters a city name.
2. The program creates an API request URL.
3. OpenWeather returns weather data in JSON format.
4. Python converts the JSON response into a dictionary.
5. The program extracts and displays the requested weather information.

## Purpose

This project was created to practice:
- Python functions
- Working with APIs
- JSON data processing
- File organization
- Handling external data sources

## License

This project is licensed under the MIT License.
