import streamlit as st

st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="Select the no of Forecasted days")
option = st.selectbox("Select the data to view",
                      ("Temperature","sky"))
st.subheader(f"{option} for the next {days} in {place}")