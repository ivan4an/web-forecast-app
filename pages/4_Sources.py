import streamlit as st

# Layout settings
page_title = "Sources"
page_icon = ":information_source:"
layout = "wide"

emoticons = "https://www.webfx.com/tools/emoji-cheat-sheet/"
data1 = "https://open-meteo.com/en"
data2 = "https://openweathermap.org/"
ivan = "https://www.linkedin.com/in/ivan-mrekaj/"
# App layout
st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout)
st.title(page_icon + " " + page_title)

st.write(f"Meteorological data: [open-meteo.com]({data1})")
st.write(f"Meteorological data: [openweathermapoorg]({data2})")
st.write(f"Emoticons: [webfx.com]({emoticons})")
st.write(f"Created by: [Ivan]({ivan})")






