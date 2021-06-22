import requests
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#stores these datas in a text file

file = open('data.txt', 'a')
file.write("-------------------------------------------------------------")
file.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
file.write("-------------------------------------------------------------")
file.write("Current Temperature   :"+str(temp_city)+'\n')
file.write("Current Weather       :"+weather_desc+'\n')
file.write("Current Humidity      :"+str(hmdt)+'\n')
file.write("Current wind speed    :"+str(wind_spd)+'\n')
file.write("Date and Time         :"+str(date_time)+'\n')
file.close()
print("-------------------------------------------------------------" +'\n')
print("DATA STORED SUCCESSFULLY"+'\n')
print("-------------------------------------------------------------")


