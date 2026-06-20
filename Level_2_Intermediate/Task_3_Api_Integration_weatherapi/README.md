# Task 3: API Integration - Weather API

## Overview
A weather application with API integration for the Codveda Python Development Internship - Level 2 Intermediate tasks.

## Description
This task involves integrating with a public weather API to fetch and display weather data for different locations.

## Features
- API request handling with proper authentication
- JSON data parsing and transformation
- Weather data display (temperature, humidity, conditions, etc.)
- Location-based queries
- Error handling for API responses
- Data caching or storage

## Requirements
- Python 3.x
- Libraries: requests
- API key from weather service (e.g., OpenWeatherMap, WeatherAPI)

## Usage
```bash
python weather_api.py <city_name>
```

Or interactive mode:
```bash
python weather_api.py
```

## Structure
- `weather_api.py` - Main application implementation
- `config.py` - Configuration and API keys (create this file)

## Configuration
Create a `config.py` file:
```python
API_KEY = "your_api_key_here"
API_BASE_URL = "https://api.weatherapi.com/v1"
```

## Learning Objectives
- Understand RESTful API architecture
- Learn to make HTTP requests to APIs
- Parse and process JSON data
- Handle API responses and errors
- Work with API authentication and keys
- Transform and format external data
- Build applications that depend on external services

## Author
Mrfe3z

## Related
This is part of the [Codveda Python Internship Portfolio](../..)

---
*Task 3 of Level 2 Intermediate - Codveda Python Development Internship*
