#Getting the data from openweathermap.org and outputing it as json file\

import requests
from tkinter import *
from PIL import ImageTk,Image

global loc

def getweatherdata(city_name):

	if city_entry.get() == '':
		
		city_name = 'Accra'

		weather_key = "065e4fee10f2926dbe94a8df021b63a0"
		url = "https://api.openweathermap.org/data/2.5/weather"
		my_parameters = {'APPID':weather_key, 'q':city_name, 'units':'metric'}


		json_requests = requests.get(url,params=my_parameters)
		json_data = json_requests.json()

		#Generate the icon
		#icon = 'http://openweathermap.org/img/wn/{}.png'.format(json_data['weather'][0]['icon'])


		humidity_label = Label(frame4,text=json_data['main']['humidity'],bg='black',fg = 'green',font=('Verdana',8) ,width=12,anchor='e').grid(row=0,column=1)
	
		air_speed_label = Label(frame5,text=json_data['wind']['speed'],bg='black',fg = 'green',font=('Verdana',8) ,width=12,anchor='e').grid(row=1,column=1)

		temperature_label = Label(frame6,text=json_data['main']['temp'],bg='black',fg = 'green',font=('Verdana',8) ,width=12,anchor='e').grid(row=2,column=1,columnspan=2)


		#Create an image object from the link
		#img = ImageTk.PhotoImage(Image.open('http://openweathermap.org/img/wn/{}.png'.format(json_data['weather'][0]['icon'])))


		#Display the icon
		#icon_label = Label(frame7,image=img).grid(row=0,column=0)

		#Clear entry after using
		city_entry.delete(0,END)


	else:

		weather_key = "065e4fee10f2926dbe94a8df021b63a0"
		url = "https://api.openweathermap.org/data/2.5/weather"
		my_parameters = {'APPID':weather_key, 'q':city_name, 'units':'metric'}


		json_requests = requests.get(url,params=my_parameters)
		json_data = json_requests.json()

		#Generate the icon
		#icon = 'http://openweathermap.org/img/wn/{}.png'.format(json_data['weather'][0]['icon'])


		humidity_label = Label(frame4,text=json_data['main']['humidity'],bg='black',fg = 'green',font=('Verdana',8) ,width=12,anchor='e').grid(row=0,column=1)
	
		air_speed_label = Label(frame5,text=json_data['wind']['speed'],bg='black',fg = 'green',font=('Verdana',8) ,width=12,anchor='e').grid(row=1,column=1)

		temperature_label = Label(frame6,text=json_data['main']['temp'],bg='black',fg = 'green',font=('Verdana',8) ,width=12,anchor='e').grid(row=2,column=1,columnspan=2)


		#Create an image object from the link
		#img = ImageTk.PhotoImage(Image.open('http://openweathermap.org/img/wn/{}.png'.format(json_data['weather'][0]['icon'])))


		#Display the icon
		#icon_label = Label(frame7,image=img).grid(row=0,column=0)

		#Clear entry after using
		city_entry.delete(0,END)

		#print(json_data)

		print(json_data)


#GUI with Tkinter
#Create the main window
mainWindow = Tk()


#Define window size
mainWindow.geometry("400x250")

#Define 6 Frames and display them on the grid
frame1 = Frame(mainWindow)
frame1.grid(row=0,column=0,columnspan=2,sticky=W,pady=(10,20),padx=(10,0))

frame2 = Frame(mainWindow)
frame2.grid(row=1,column=0,columnspan=2,sticky=W,pady=(0,10),padx=(10,0))

frame3 = Frame(mainWindow)
frame3.grid(row=2,column=0,columnspan=2,sticky=W,pady=(0,10),padx=(10,0))

frame4 = Frame(mainWindow)
frame4.grid(row=3,column=0,columnspan=2,sticky=W,pady=(0,10),padx=(10,0))

frame5 = Frame(mainWindow)
frame5.grid(row=4,column=0,columnspan=2,sticky=W,pady=(0,10),padx=(10,0))

frame6 = Frame(mainWindow)
frame6.grid(row=5,column=0,columnspan=2,sticky=W,pady=(0,10),padx=(10,0))

#frame7 = Frame(mainWindow)
#frame7.grid(row=5,column=0,columnspan=2,sticky=W,pady=(0,10),padx=(10,0))


#Create the first label
prompt_label = Label(frame1,text='Enter City Name Below:')
prompt_label.grid(row=0,column=0)

#Create the second label which has the entry and the button in the second frame
#Entry Label
city_entry = Entry(frame2,width=20,bg = 'black',fg = 'yellow')
city_entry.grid(row=0,column=0,padx=(0,25))


#Button widget
get_city_button = Button(frame2,text='Weather Data Info',command=lambda:getweatherdata(city_entry.get()))
get_city_button.grid(row=0,column=2)


#Create the third Label in the third frame
#Label widget
#data_for_given_city = Label(frame3,text='Data for :' + str(city_entry.get()))
#data_for_given_city.grid(row=0,column=0)

#Create the fourth frame
#Label widget
humidity = Label(frame4,text='Humidity').grid(row=0,column=0,padx=(0,100))
#humidity_label = Label(frame4,text=city_entry.get(),bg='black',fg = 'red' ,width=12).grid(row=0,column=1)

air_speed = Label(frame5,text='Air Speed').grid(row=1,column=0,padx=(0,100))
#air_speed_label = Label(frame5,text=city_entry.get(),bg='black',fg = 'red' ,width=12).grid(row=1,column=1)

temperature = Label(frame6,text='Temperature').grid(row=2,column=0,padx=(0,82))
#temperature_label = Label(frame6,text=city_entry.get(),bg='black',fg = 'red' ,width=12).grid(row=2,column=1,columnspan=2)

mainWindow.mainloop()



