import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from webbrowser import Mozilla
import os
import random
import subprocess
from PyDictionary import PyDictionary
import requests
import json
# webbrowser.get(using=None)
# webbrowser.register(name, constructor, instance=None, preferred=False)
Mozilla('mozilla')


dictionary = PyDictionary()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print (voices)
engine.setProperty('rate', 175)
engine.setProperty('volume', 2)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak('Good Morning! Aditya')
	elif hour > 12 and hour < 18:
		speak("Good Afternoon! Aditya")
	else:
		speak("Good Evening! Aditya")

	speak("I am Alexa, your Assistent, How can I help you?")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print("User said => ", query)
		print("")

	except Exception as e:
		print(e)
		print("Sorry! Can you say that again Please...")
		return 'None'
	return query

if __name__ == "__main__":
	wishMe()
	while True:
		query = takeCommand().lower()

		#Logic to perform tasks
		if 'wikipedia' in query:
			speak("Searching Wikipedia...")
			query = query.replace('wikipedia', "")
			results = wikipedia.summary(query, sentences = 2)
			print(results.encode("utf-8"))
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open('youtube.com')

		elif 'open google' in query:
			webbrowser.open('google.com')

		elif 'open stack overflow' in query:
			webbrowser.open('stackoverflow.com')

		elif 'open bing' in query:
			webbrowser.open('bing.com')

		elif 'open facebook' in query:
			webbrowser.open("facebook.com")

		elif "open powershell" in query:
			subprocess.Popen("C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe")

		elif 'play music' in query:
			music_dir = "C:\\Users\\NC\\Music"
			songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
			n_music = (len([name for name in [f for f in os.listdir(music_dir) if f.endswith('.mp3')] if os.path.isfile(os.path.join(music_dir, name))]))
			os.startfile(os.path.join(music_dir, songs[random.randint(0, n_music-1)]))
			# playsound()

		elif 'the time' in query:
			timeNow = datetime.datetime.now().strftime("%H:%M:%S")
			print("Time is => ", timeNow)
			speak(timeNow)

		elif 'open notepad' in query:
			print("Opening Notepad...")
			subprocess.Popen("C:\\Windows\\system32\\notepad.exe")

		elif 'what is the meaning of' in query:
			query = query.replace("what is the meaning of ", "")
			result_dict = (dictionary.meaning(query))
			# print(type(result_dict))
			var1 = 'Noun'
			topic = result_dict[var1]
			print(topic)
			speak(topic)


		elif 'weather' in query:
			print("Getting Weather Details...")
			speak("Getting Weather Details...")

			# #Assigning URL Variables to get the data from
			api_key = "7e3be4550956ad86c30858a5a89d1ba9"
			base_url = "http://api.openweathermap.org/data/2.5/weather?"
			city = "lucknow"
			complete_url = base_url + "appid=" + api_key + "&q=" + city

			response = requests.get(complete_url)
			x = response.json()

			if x["cod"] != "404":

					y = x["main"]

					current_temperature = y["temp"]

					current_pressure = y["pressure"]
					current_humidiy = y["humidity"]
					z = x["weather"]
					weather_description = z[0]["description"]
					print(" Temperature (in celcius) = " +
									str(round(int(current_temperature) - 273.15)) + "' C" +
							"\n humidity (in percentage) = " +
									str(current_humidiy) +
							"\n description = " +
									str(weather_description))

					speak(" Temperature (in Lucknow) is " +
 				                    str(round(int(current_temperature) - 273.15)) + "degrees Centigrate")

			else:
				print(" City Not Found ")

		elif 'exit' in query:
			print("Thank you ! ")
			speak("Thank you")
			break
			
