import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import backend as bd

# LAYOUT SETTINGS
page_title = "Air composition"
page_title_2 = "Air Composition Forecast"
page_icon = ":mask:"
layout = "wide"

# APP LAYOUT
st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout)
st.title(page_title_2)
st.info("""
**_Note:_**  You can turn off and turn on lines in each graph by clicking 
on the plot legend.
""")

# CURRENT TIME
current_time = st.session_state['current_time']

# DATA
location = st.session_state['location']
latitude = location[0]
longitude = location[1]

# Data for graph of meteo forecast
air_data = bd.get_air_composition_data(latitude, longitude)
air_dates = air_data['hourly']['time']
pm10 = air_data['hourly']['pm10']
pm2_5 = air_data['hourly']['pm2_5']
carbon_monoxide = air_data['hourly']['carbon_monoxide']
nitrogen_dioxide = air_data['hourly']['nitrogen_dioxide']
sulphur_dioxide = air_data['hourly']['sulphur_dioxide']
ozone = air_data['hourly']['ozone']
pollen_dates = air_data['hourly']['time'][:96]
alder_pollen = air_data['hourly']['alder_pollen']
birch_pollen = air_data['hourly']['birch_pollen']
grass_pollen = air_data['hourly']['grass_pollen']
mugwort_pollen = air_data['hourly']['mugwort_pollen']
olive_pollen = air_data['hourly']['olive_pollen']
ragweed_pollen = air_data['hourly']['ragweed_pollen']
european_aqi = air_data['hourly']['european_aqi']

# Create air composition plot
air_fig = go.Figure()
# Add pm10
air_fig.add_trace(
        go.Scatter(x=air_dates, y=pm10,
                   name="pm10",
                   marker_color=px.colors.qualitative.G10[3]
                   )
)
# Add pm2.5
air_fig.add_trace(
        go.Scatter(x=air_dates, y=pm2_5,
                   name="pm2.5",
                   marker_color=px.colors.qualitative.G10[7]
                   )
)
air_fig.add_trace(
        go.Scatter(x=air_dates, y=carbon_monoxide,
                   name="carbon monoxide",
                   marker_color=px.colors.qualitative.G10[5]
                   )
)
air_fig.add_trace(
        go.Scatter(x=air_dates, y=nitrogen_dioxide,
                   name="nitrogen dioxide",
                   marker_color=px.colors.qualitative.G10[6]
                   )
)
air_fig.add_trace(
        go.Scatter(x=air_dates, y=sulphur_dioxide,
                   name="sulphur dioxide",
                   marker_color=px.colors.qualitative.G10[2]
                   )
)
air_fig.add_trace(
        go.Scatter(x=air_dates, y=ozone,
                   name="ozone",
                   marker_color=px.colors.qualitative.G10[9]
                   )
)
# Add current time
air_fig.add_vline(x=current_time,
                      line_width=1,
                      line_dash="dot",
                      line_color="red"
                      )
# Update axis names, hover, legend
air_fig.update_layout(
        title=dict(text="<b>Air composition</b> (μg/m³)"),
        xaxis_title="Date",
        yaxis_title="μg/m³",
        hovermode='x',
        legend=dict(orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                    )
)

# Create pollen situation plot
pollen_fig = go.Figure()
pollen_fig.add_trace(
        go.Scatter(x=pollen_dates, y=alder_pollen,
                   name="alder pollen",
                   marker_color=px.colors.qualitative.Dark2[7]
                   )
)
pollen_fig.add_trace(
        go.Scatter(x=pollen_dates, y=birch_pollen,
                   name="birch pollen",
                   marker_color=px.colors.qualitative.Dark2[6]
                   )
)
pollen_fig.add_trace(
        go.Scatter(x=pollen_dates, y=grass_pollen,
                   name="grass pollen",
                   marker_color=px.colors.qualitative.Dark2[0]
                   )
)
pollen_fig.add_trace(
        go.Scatter(x=pollen_dates, y=olive_pollen,
                   name="olive pollen",
                   marker_color=px.colors.qualitative.Dark2[4]
                   )
)
pollen_fig.add_trace(
        go.Scatter(x=pollen_dates, y=mugwort_pollen,
                   name="mugwort pollen",
                   marker_color=px.colors.qualitative.Dark2[1]
                   )
)
pollen_fig.add_trace(
        go.Scatter(x=pollen_dates, y=ragweed_pollen,
                   name="ragweed pollen",
                   marker_color=px.colors.qualitative.Dark2[3]
                   )
)
# Add current time
pollen_fig.add_vline(x=current_time,
                     line_width=1,
                     line_dash="dot",
                     line_color="red"
                     )
# Update axis names, hover, legend
pollen_fig.update_layout(
        title=dict(text="<b>Pollen in the Air</b> (grains/m³)"),
        xaxis_title="Date",
        yaxis_title="grains/m³",
        hovermode='x',
        legend=dict(orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                    )
)

# Show plot in app and set auto resize with browser window
st.plotly_chart(air_fig, use_container_width=True)
st.info("""
Pollen forecast is only available for Europe during pollen season.""")
st.plotly_chart(pollen_fig, use_container_width=True)


