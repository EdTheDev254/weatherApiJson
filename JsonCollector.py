#This was the first python file for testing the api call

import requests

#make a function to collect the json file 
#with a parameter of the city's or capital city's
#name

def get_json (city) :
	#weather key needs updating! 

	weather_key = "76b9baa188dca2b6a27a92c2d09404c8"
	parameters = {"APPID" :weather_key,"q" :city, "units" :"metric"}
	url = "http://api.openweathermap.org/data/2.5/weather"
	response_data = requests.get(url, params = parameters) 
	json_output = response_data.json()
	
	return json_output

city_name=input("Enter country's or capital city's name:" )
print("Json data below:\n")
print(get_json(city_name))
