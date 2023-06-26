import requests

api_key = "9d7cde1f6d07ec55650544be1631307e"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = "coimbatore"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
print(response.text)