import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input,slider, selectbox and subheader
st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the no of Forecasted days")

option = st.selectbox("Select the data to view",
                      ("Temperature", "sky"))
st.subheader(f"{option} for the next {days} in {place}")
if place:
# get the temperature/sky data
    try:
        filtered_data = get_data(place, days)

        # create a temperature plot
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date","y":"Temperature (C)"})
            st.plotly_chart(figure)
        if option == "sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place doesn't exist.")
