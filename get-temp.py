import sys
import requests

def getWeatherData(loc):
	weather_key = "065e4fee10f2926dbe94a8df021b63a0"
	url = "https://api.openweathermap.org/data/2.5/weather"
	my_parameters = {'APPID':weather_key,'q':loc,'units':'metric'}

	try:
		get_json = requests.get(url,params=my_parameters) #make an api call
		json_data = get_json.json() #convert to json type

		return "Temperature for {} is:{} degrees Celcius".format(loc,json_data['main']['temp'])

	except:
		return "No temperature data for {}!".format(loc)

#If no argument has been passed then set to a default parameter 
if len(sys.argv) <= 1:
	print("No argument passed,deafult parameter set as:Accra!")
	print(getWeatherData("Accra"))

else:
	n = len(sys.argv)

	for i in range(1,n):
		print(getWeatherData(sys.argv[i]))
