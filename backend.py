import requests
API_KEY ='cfebab5f173043bea4cbbc9829030919'
def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value = 8 * forecast_days
    filtered_data = filtered_data[:nr_value]
    if kind == "Temperature":
        filtered_data=[dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return data

if __name__=="__main__":
    print(get_data(place="Tokyo",forecast_days=3,kind="sky"))