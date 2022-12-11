import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# LAYOUT SETTINGS
page_title = "Meteorological Forecast"
page_icon = ":partly_sunny:"
layout = "wide"

# APP LAYOUT
st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout)
st.title(page_title + " " + page_icon)
st.info("""
**_Note:_**  You can turn off and turn on lines in each graph by clicking 
on the plot legend.
""")

# CURRENT TIME
current_time = st.session_state['current_time']
# METEO DATA
meteo_data = st.session_state['meteo_data']
meteo_dates = meteo_data['hourly']['time']
temperature = meteo_data['hourly']['temperature_2m']
apparent_temperature = meteo_data['hourly']['apparent_temperature']
precipitation = meteo_data['hourly']['precipitation']
windspeed_10m = meteo_data['hourly']['windspeed_10m']
windgusts_10m = meteo_data['hourly']['windgusts_10m']
winddirection_10m = meteo_data['hourly']['winddirection_10m']

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
temperature_fig.add_trace(
        go.Scatter(x=meteo_dates, y=apparent_temperature,
                   name="Feels-like temperature",
                   marker_color=px.colors.qualitative.Dark24[7]
                   )
)
temperature_fig.add_vline(x=current_time,
                          line_width=1,
                          line_dash="dot",
                          line_color="red"
                          )
temperature_fig.update_layout(
        title=dict(text="<b>Temperature</b> (°C)"),
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
        go.Bar(x=meteo_dates, y=precipitation,
               name="Precipitation",
               marker_color=px.colors.qualitative.Dark24[0]
               )
)
precipitation_fig.add_vline(x=current_time,
                            line_width=1,
                            line_dash="dot",
                            line_color="red"
                            )
precipitation_fig.update_layout(
        title=dict(text="<b>Precipitation</b> (mm)"),
        xaxis=dict(title="Date",
                   ),
        yaxis=dict(title="precipitation (mm)",
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
# Create wind plot
wind_fig = go.Figure()
wind_fig.add_trace(
        go.Scatter(x=meteo_dates, y=windspeed_10m,
                   name="Wind speed",
                   marker_color=px.colors.qualitative.Dark24[22]
                   )
)
wind_fig.add_trace(
        go.Bar(x=meteo_dates, y=windgusts_10m,
               name="Wind gusts",
               marker_color=px.colors.qualitative.Dark24[8]
               )
)
wind_fig.add_vline(x=current_time,
                   line_width=1,
                   line_dash="dot",
                   line_color="black"
                   )
wind_fig.update_layout(
        title=dict(text="<b>Wind speed and wind gusts</b> (km/h)"),
        xaxis=dict(title="Date",
                   ),
        yaxis=dict(title="wind speed (km/h)",
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
# Create wind direction plot
winddirection_fig = go.Figure()
winddirection_fig.add_trace(
        go.Scatter(x=meteo_dates, y=winddirection_10m,
                   name="Wind direction in degrees",
                   marker_color=px.colors.qualitative.Dark24[3],
                   mode="markers"
                   )
)
winddirection_fig.add_vline(x=current_time,
                            line_width=1,
                            line_dash="dot",
                            line_color="black"
                            )
winddirection_fig.update_layout(
        title=dict(text="<b>Wind direction</b> (°)"),
        xaxis=dict(title="Date",
                   ),
        yaxis=dict(title="wind direction (°)",
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
st.plotly_chart(wind_fig, use_container_width=True)
st.plotly_chart(winddirection_fig, use_container_width=True)
