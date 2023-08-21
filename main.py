import streamlit as st
import plotly.express as px

st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="Select the no of Forecasted days")
option = st.selectbox("Select the data to view",
                      ("Temperature","sky"))
st.subheader(f"{option} for the next {days} in {place}")

def get_data(days):
    dates = ["2022-01-23","2023-09-19","2021-09-23"]
    temperatures = [10,12,14]
    temperatures = [days*i for i in temperatures]
    return dates,temperatures

d, t = get_data(days)

figure=px.line(x=d, y=t, labels={"x":"Date","y":"Temperature (C)"})
st.plotly_chart(figure)