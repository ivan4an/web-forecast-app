import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# LAYOUT SETTINGS
page_title = "Forestry and Agriculture"
page_title_2 = "Meteorological Forecast for Forestry and Agriculture"
page_icon = ":deciduous_tree:"
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

try:
    # CURRENT TIME
    current_time = st.session_state['current_time']

    # DATA
    meteo_data = st.session_state['meteo_data']
    meteo_dates = meteo_data['hourly']['time']
    temperature = meteo_data['hourly']['temperature_2m']
    precipitation = meteo_data['hourly']['precipitation']
    evapotranspiration = meteo_data['hourly']['evapotranspiration']
    soil_temperature_0cm = meteo_data['hourly']['soil_temperature_0cm']
    soil_temperature_6cm = meteo_data['hourly']['soil_temperature_6cm']
    soil_temperature_18cm =meteo_data['hourly']['soil_temperature_18cm']


    soil_moisture_0_1cm = meteo_data['hourly']['soil_moisture_0_1cm']
    soil_moisture_9_27cm = meteo_data['hourly']['soil_moisture_9_27cm']
    soil_moisture_27_81cm = meteo_data['hourly']['soil_moisture_27_81cm']

    # PLOTS
    # Create temperature plot
    temperature_fig = go.Figure()
    # Add temperature as line plot
    temperature_fig.add_trace(
            go.Scatter(x=meteo_dates, y=temperature,
                       name="Temperature",
                       marker_color=px.colors.qualitative.Dark24[5]
                       )
    )
    temperature_fig.add_vline(x=current_time,
                              line_width=1,
                              line_dash="dot",
                              line_color="red"
                              )
    temperature_fig.update_layout(
            title=dict(text="<b>Temperature</b> (°C)"
                       ),
            xaxis=dict(title="Date",
                       ),
            yaxis=dict(title="temperature (°C)",
                       titlefont=dict(color="black"),
                       tickfont=dict(color="black")
                       ),
            hovermode='x',
            legend=dict(orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                        )
    )
    # Create precipitation plot
    precipitation_fig = go.Figure()
    precipitation_fig.add_trace(
            go.Scatter(x=meteo_dates, y=precipitation,
                       name="precipitation",
                       marker_color=px.colors.qualitative.Dark24[9]
                       )
    )
    precipitation_fig.add_trace(
            go.Scatter(x=meteo_dates, y=evapotranspiration,
                       name="evapotranspiration",
                       marker_color=px.colors.qualitative.Dark24[3]
                       )
    )
    precipitation_fig.add_vline(x=current_time,
                                line_width=1,
                                line_dash="dot",
                                line_color="red"
                                )
    precipitation_fig.update_layout(
            title=dict(text="<b>Precipitation and Evapotranspiration</b> (mm)"),
            xaxis=dict(title="Date",
                       ),
            yaxis=dict(title="precipitation and evapotranspiration (mm)",
                       titlefont=dict(color="black"),
                       tickfont=dict(color="black")
                       ),
            hovermode='x',
            legend=dict(orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                        )
    )
    # Create soil temperature plot
    soiltemperature_fig = go.Figure()
    soiltemperature_fig.add_trace(
            go.Scatter(x=meteo_dates, y=soil_temperature_0cm,
                       name="soil temperature 0 cm",
                       marker_color=px.colors.qualitative.Antique[1]
                       )
    )
    soiltemperature_fig.add_trace(
            go.Scatter(x=meteo_dates, y=soil_temperature_6cm,
                       name="soil temperature 6 cm",
                       marker_color=px.colors.qualitative.Antique[2]
                       )
    )
    soiltemperature_fig.add_trace(
            go.Scatter(x=meteo_dates, y=soil_temperature_18cm,
                       name="soil temperature 18 cm",
                       marker_color=px.colors.qualitative.Antique[3]
                       )
    )
    soiltemperature_fig.add_vline(x=current_time,
                                  line_width=1,
                                  line_dash="dot",
                                  line_color="red"
                                  )
    soiltemperature_fig.update_layout(
            title=dict(text="<b>Soil temperature in depth 0, 6, 18 cm</b> (°C)"),
            xaxis=dict(title="Date",
                       ),
            yaxis=dict(title="soil temperature (°C)",
                       titlefont=dict(color="black"),
                       tickfont=dict(color="black")
                       ),
            hovermode='x',
            legend=dict(orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                        )
    )
    # Create soil moisture plot
    soilmoisture_fig = go.Figure()
    soilmoisture_fig.add_trace(
            go.Scatter(x=meteo_dates, y=soil_moisture_0_1cm,
                       name="soil moisture 0-1 cm",
                       marker_color=px.colors.qualitative.Antique[1]
                       )
    )
    soilmoisture_fig.add_trace(
            go.Scatter(x=meteo_dates, y=soil_moisture_9_27cm,
                       name="soil moisture 9-27 cm",
                       marker_color=px.colors.qualitative.Antique[2]
                       )
    )
    soilmoisture_fig.add_trace(
            go.Scatter(x=meteo_dates, y=soil_moisture_27_81cm,
                       name="soil moisture 27-81 cm",
                       marker_color=px.colors.qualitative.Antique[3]
                       )
    )
    soilmoisture_fig.add_vline(x=current_time,
                               line_width=1,
                               line_dash="dot",
                               line_color="red"
                               )
    soilmoisture_fig.update_layout(
            title=dict(text="<b>Soil moisture</b> (m³/m³)"),
            xaxis=dict(title="Date",
                       ),
            yaxis=dict(title="soil moisture  (m³/m³)",
                       titlefont=dict(color="black"),
                       tickfont=dict(color="black")
                       ),
            hovermode='x',
            legend=dict(orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                        )
    )
    # Show plots in app and auto resize with window
    st.plotly_chart(temperature_fig, use_container_width=True)
    st.plotly_chart(precipitation_fig, use_container_width=True)
    st.plotly_chart(soiltemperature_fig, use_container_width=True)
    st.plotly_chart(soilmoisture_fig, use_container_width=True)
except (KeyError) as error:
    st.markdown("Go to the main page and **select location**!")

