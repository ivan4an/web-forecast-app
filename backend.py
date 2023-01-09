import requests
import pandas as pd
import streamlit as st
import os

API_KEY_LOCATION = os.getenv("API_METEO")
#API_KEY_LOCATION = st.secrets["API_KEY_LOCATION"]
BINS = [0, 22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5, 360]
LABELS = ["North", "Notheast", "East", "Southeast", "South",
           "Southwest", "West", "Northwest", "north"]
WEATHER_CODE = [0, 1, 2, 3, 45, 48, 51, 53, 55, 56, 57, 61, 63, 65, 66,
                67, 71, 73, 75, 77, 80, 81, 82, 85, 86, 95, 96, 99]
DESCRIPTION = ["clear sky", "mainly clear", "partly cloudy", "overcast",
               "fog", "depositing rime fog", "light drizzle",
               "moderate drizzle", "drizzle with dense intensity",
               "light freezing drizzle",
               "freezing drizzle with dense intensity", "slight rain",
               "moderate rain", "rain with heavy intensity",
               "light freezing rain", "freezing rain with heavy intensity",
               "slight snow fall", "moderate snow fall",
               "snow fall with heavy intensity", "snow grains",
               "slight rain showers", "moderate rain showers",
               "violent rain showers", "slight snow showers",
               "heavy snow showers", "thunderstorm",
               "thunderstorm with slight hail", "thunderstorm with heavy hail"]
DF_WEATHER_CODE = pd.DataFrame(list(zip(WEATHER_CODE, DESCRIPTION)),
                               columns=['weather_code',
                                        'weather_description'])


def get_air_composition_data(latitude, longitude):
    url = f"https://air-quality-api.open-meteo.com/v1/air-quality?" \
          f"latitude={latitude}&" \
          f"longitude={longitude}&" \
          f"hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide," \
          f"ozone,alder_pollen,birch_pollen,grass_pollen,mugwort_pollen," \
          f"olive_pollen,ragweed_pollen,european_aqi"
    response = requests.get(url)
    data = response.json()
    return data


def get_meteo_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?" \
          f"latitude={latitude}&" \
          f"longitude={longitude}&" \
          f"hourly=temperature_2m,relativehumidity_2m,apparent_temperature," \
          f"precipitation,weathercode,cloudcover,cloudcover_low," \
          f"cloudcover_mid,cloudcover_high,evapotranspiration," \
          f"soil_temperature_0cm,soil_temperature_6cm,soil_temperature_18cm," \
          f"soil_moisture_0_1cm,soil_moisture_9_27cm,soil_moisture_27_81cm," \
          f"windspeed_10m,winddirection_10m,windgusts_10m&" \
          f"models=best_match&" \
          f"daily=temperature_2m_max,temperature_2m_min,sunrise,sunset," \
          f"precipitation_sum,windspeed_10m_max,winddirection_10m_dominant&" \
          f"current_weather=true&timezone=auto"
    response = requests.get(url)
    data = response.json()
    return data


def get_location(lat, lng):
    return lat, lng


def get_location_data(latitude, longitude, limit=0):
    url = f"http://api.openweathermap.org/geo/1.0/reverse?" \
          f"lat={latitude}&" \
          f"lon={longitude}&" \
          f"limit={limit}&a" \
          f"ppid={API_KEY_LOCATION}"
    response = requests.get(url)
    data = response.json()[0]
    return data


if __name__ == "__main__":
    data = get_location_data(27.877077, -0.285319)
    print(data)