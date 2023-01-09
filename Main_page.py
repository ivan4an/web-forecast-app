import streamlit as st
import folium as fl
from streamlit_folium import st_folium
import pandas as pd
import datetime
import backend as bd

# LAYOUT SETTINGS
page_title = "Weather Forecast App"
page_icon = ":partly_sunny:"
layout = "wide"

# APP LAYOUT
st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout)
st.title(page_title + " " + page_icon)

# INPUTS
# Map for selection of location
my_map = fl.Map()
my_map.add_child(fl.LatLngPopup())
map_show = st_folium(my_map, height=350, width=700)

# RUN APP
try:
    # Get coordinates
    location = bd.get_location(map_show['last_clicked']['lat'],
                               map_show['last_clicked']['lng'])
    latitude = round(location[0], 4)
    longitude = round(location[1], 4)
    # Get current time
    current_time = datetime.datetime.now()

    # METEO DATA
    # Get meteo data
    meteo_data = bd.get_meteo_data(latitude, longitude)
    # CURRENT WEATHER
    # Extract data for current weather
    current_temperature = meteo_data['current_weather']['temperature']
    current_windspeed = meteo_data['current_weather']['windspeed']
    current_winddirection = meteo_data['current_weather']['winddirection']
    current_weathercode = meteo_data['current_weather']['weathercode']
    # Convert wind direction and current weather code
    # from number code to text
    current_winddirection_text = pd.cut([current_winddirection],
                                        bins=bd.BINS, labels=bd.LABELS)[0]
    current_weathercode_text = bd.DF_WEATHER_CODE[
        bd.DF_WEATHER_CODE['weather_code']
        == current_weathercode]['weather_description'].values[0]

    # Show the information about current weather
    st.subheader("Current weather")
    st.markdown(f"**{current_weathercode_text.capitalize()}**. "
                f"Temperature is **{current_temperature} °C**. "
                f"**{current_winddirection_text.capitalize()}** "
                f"wind is blowing at a speed "
                f"**{current_windspeed} km/h**.")

    # FORECAST FOR THE NEXT THREE DAYS
    # TODAY
    today_date = meteo_data['daily']['time'][0]
    today_day = pd.Timestamp(today_date).day_name()
    today_sunrise = meteo_data['daily']['sunrise'][0][-5:]
    today_sunset = meteo_data['daily']['sunset'][0][-5:]
    today_min_t = meteo_data['daily']['temperature_2m_min'][0]
    today_max_t = meteo_data['daily']['temperature_2m_max'][0]
    today_precipitation_sum = meteo_data['daily']['precipitation_sum'][0]
    today_dominant_winddirection = \
        meteo_data['daily']['winddirection_10m_dominant'][0]
    today_dominant_winddirection_text = pd.cut([today_dominant_winddirection],
                                               bins=bd.BINS,
                                               labels=bd.LABELS)[0]
    today_max_windspeed = meteo_data['daily']['windspeed_10m_max'][0]
    # Title of the section
    st.subheader(f"Forecast for today and the next two days")
    # Show the forecast for today
    st.info(f" **{today_day}** _(today)_")
    st.markdown(f"""
    :sunrise: Sunrise: **{today_sunrise}** :sunrise_over_mountains: Sunset: **{today_sunset}**\n
    🌡 Temperature: from **{today_min_t}** to **{today_max_t} °C**\n
    :droplet: Precipitation sum: **{today_precipitation_sum} mm**\n
    💨 Maximum wind speed: **{today_max_windspeed} km/h**\n
    :wind_chime: Dominant wind direction: **{today_dominant_winddirection_text.capitalize()}**
    """)

    # TOMORROW
    tomorrow_date = meteo_data['daily']['time'][1]
    tomorrow_day = pd.Timestamp(tomorrow_date).day_name()
    tomorrow_sunrise = meteo_data['daily']['sunrise'][1][-5:]
    tomorrow_sunset = meteo_data['daily']['sunset'][1][-5:]
    tomorrow_min_t = meteo_data['daily']['temperature_2m_min'][1]
    tomorrow_max_t = meteo_data['daily']['temperature_2m_max'][1]
    tomorrow_precipitation_sum = meteo_data['daily']['precipitation_sum'][1]
    tomorrow_dominant_winddirection = \
        meteo_data['daily']['winddirection_10m_dominant'][1]
    tomorrow_dominant_winddirection_text = pd.cut(
        [tomorrow_dominant_winddirection],
        bins=bd.BINS,
        labels=bd.LABELS)[0]
    tomorrow_max_windspeed = meteo_data['daily']['windspeed_10m_max'][1]
    # Show the forecast for tomorrow
    st.info(f" **{tomorrow_day}** _(tomorrow)_")
    st.markdown(f"""
    :sunrise: Sunrise: **{tomorrow_sunrise}** :sunrise_over_mountains: Sunset: **{tomorrow_sunset}**\n
    🌡 Temperature: from **{tomorrow_min_t}** to **{tomorrow_max_t} °C**\n
    :droplet: Precipitation sum: **{tomorrow_precipitation_sum} mm**\n
    💨 Maximum wind speed: **{tomorrow_max_windspeed} km/h**\n
    :wind_chime: Dominant wind direction: **{tomorrow_dominant_winddirection_text.capitalize()}**
        """)

    # DAY AFTER TOMORROW
    dat_date = meteo_data['daily']['time'][2]
    dat_day = pd.Timestamp(dat_date).day_name()
    dat_sunrise = meteo_data['daily']['sunrise'][2][-5:]
    dat_sunset = meteo_data['daily']['sunset'][2][-5:]
    dat_min_t = meteo_data['daily']['temperature_2m_min'][2]
    dat_max_t = meteo_data['daily']['temperature_2m_max'][2]
    dat_precipitation_sum = meteo_data['daily']['precipitation_sum'][2]
    dat_dominant_winddirection = \
        meteo_data['daily']['winddirection_10m_dominant'][2]
    dat_dominant_winddirection_text = pd.cut(
        [dat_dominant_winddirection],
        bins=bd.BINS,
        labels=bd.LABELS)[0]
    dat_max_windspeed = meteo_data['daily']['windspeed_10m_max'][2]

    # Show the forecast for the next three days
    # Show the forecast for tomorrow
    st.info(f" **{dat_day}** _(day after tomorrow)_")
    st.markdown(f"""
    :sunrise: Sunrise: **{dat_sunrise}** :sunrise_over_mountains: Sunset: **{dat_sunset}**\n
    🌡 Temperature: from **{dat_min_t}** to **{dat_max_t} °C**\n
    :droplet:Precipitation sum: **{dat_precipitation_sum} mm**\n
    💨 Maximum wind speed: **{dat_max_windspeed} km/h**\n
    :wind_chime: Dominant wind direction: **{dat_dominant_winddirection_text.capitalize()}**
            """)
    # Save coordinates and current time into session statement
    st.session_state['location'] = location
    st.session_state['meteo_data'] = meteo_data
    st.session_state['current_time'] = current_time
except (TypeError, IndexError) as error:
    st.markdown("Click to **select location**!")







