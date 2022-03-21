from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("WeatherGUI")
root.geometry("312x330")
root.configure(background="#89CFF0")

img1 = ImageTk.PhotoImage(Image.open("Clear.png").resize((220,159), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("Clouds.png").resize((220,159), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open("Rain.png").resize((220,159), Image.ANTIALIAS))
img4 = ImageTk.PhotoImage(Image.open("Snow.png").resize((220,159), Image.ANTIALIAS))
img5 = ImageTk.PhotoImage(Image.open("Wrongcity.png").resize((220,159), Image.ANTIALIAS))

def get_results(city):
	try:
		owm = OWM('59e00122f624113f6b42fc41de074306')
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(city)

		w = observation.weather
		temperature = w.temperature('celsius')['temp']
		weather = w.status
		wind = w.wind()['speed']

		showweather = "🏙City: " + city.title() + "\
					 \n🌡Current temperature: " + str(temperature) + "℃\n🍃Current wind speed: " + str(wind) + "m/s\n☁Weather: " + weather.capitalize()

		if weather == "Snow":
			snowimg = Label(image=img4)
			snowimg.place(x=50, y=45)
		elif weather == "Clear":
			clearimg = Label(image=img1)
			clearimg.place(x=50, y=45)
		elif weather in ("Clouds", "Mist"):
			cloudsimg = Label(image=img2)
			cloudsimg.place(x=50, y=45)
		else:
			rainimg = Label(image=img3)
			rainimg.place(x=50, y=45)

		showresults.delete(0.0, END)
		showresults.insert(0.0, showweather)
	except:
		errorimg = Label(image=img5)
		errorimg.place(x=50, y=45)
		showresults.delete(0.0, END)
		showresults.insert(0.0, "Unable to find city.\nPlease check your spelling")


Label(root, text="Enter a city: ", bg="#89CFF0", font=("Helvetica",11)).grid(row=0, column=0, sticky=W)
city = Entry(root, width=23)
bttn = Button(root, text="    🔍    ", bg="#7393B3", command=lambda: get_results(city.get()), font=("Helvetica",11))
showresults = Text(root, width=36, height=6, borderwidth=3)
city.grid(row=0, column=1, sticky=W)
bttn.grid(row=0, column=2, padx=5, sticky=W)
Label(root, text="\n\n\n\n\n\n\n\n\n\n\n", bg="#89CFF0").grid(row=1)
showresults.place(x=7, y=220)


root.mainloop()