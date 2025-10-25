import datetime
import speech_recognition as sr
import webbrowser
import pyjokes
import pyttsx3
import time
import wikipedia
import requests
from tkinter import *
from tkinter import messagebox

def listen_and_convert():
 while True:


    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Jarvis: Listening... Please speak something!")

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Jarvis: Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Jarvis: Sorry, I'm having trouble connecting to the service.")
def speech(x):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1)
    engine.say(x)
    engine.runAndWait()
if __name__ == '__main__':
    speech("Hello! I am jarvis, your voice  assistant.")

    while True:
        data = listen_and_convert().lower()

        if data:
            if "your name" in data:
                name = "My name is jarvis."
                speech(name)
            elif "time" in data:
                current_time = datetime.datetime.now().strftime("%I%M%p")
                speech(current_time)
                print(current_time)
            elif "date" in data:
                current_date = datetime.datetime.now().strftime("%A%B%d%Y")
                speech(current_date)
                print(current_date)
            elif "youtube" in data:
                webbrowser.open("https://www.youtube.com/")
            elif "google" in data:
                webbrowser.open("https://www.google.com/")
            elif "whatsapp" in data:
                webbrowser.open("https://web.whatsapp.com/")
            elif "netflix" in data:
                webbrowser.open("https://www.netflix.com/")
            elif "chatgpt" in data:
                webbrowser.open("https://chatgpt.com/")
            elif "joke" in data:
                joke1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke1)
                speech(joke1)
            elif "wikipedia" in data:
                user_request = data.replace("jarvis ", "")
                user_request = user_request.replace("search wikipedia ", "")
                print(user_request)

                result = wikipedia.summary(user_request, sentences=1)
                print(result)
                speech(result)
            elif "weather" in data:
                speech("enter city name")
                def get_weather():
                    city = city_entry.get()
                    if city:
                        api_key = "insert-your-api-key-here"
                        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

                        try:
                            response = requests.get(base_url)
                            data = response.json()

                            if response.status_code == 200:
                                main = data['main']
                                weather = data['weather'][0]
                                wind = data['wind']

                                temp = main['temp']
                                pressure = main['pressure']
                                humidity = main['humidity']
                                description = weather['description']
                                wind_speed = wind['speed']

                                result_label.config(
                                    text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa\n"
                                         f"Weather: {description.capitalize()}\nWind Speed: {wind_speed} m/s")

                            else:
                                messagebox.showerror("Error", "City not found or invalid API request.")
                        except Exception as e:
                            messagebox.showerror("Error", f"An error occurred: {e}")
                    else:
                        messagebox.showwarning("Input Required", "Please enter a city name.")


                root = Tk()
                root.title("Weather App")
                root.geometry("400x400")
                root.config(bg="light blue")

                title_label = Label(root, text="Weather App", font=("Helvetica", 24, "bold"), bg="light blue")
                title_label.pack(pady=20)

                city_label = Label(root, text="Enter City Name:", font=("Helvetica", 12), bg="light blue")
                city_label.pack(pady=10)
                city_entry = Entry(root, font=("Helvetica", 12), width=25)
                city_entry.pack(pady=5)

                get_weather_button = Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather)
                get_weather_button.pack(pady=20)

                result_label = Label(root, text="", font=("Helvetica", 12), bg="light blue")
                result_label.pack(pady=10)

                root.mainloop()
            elif  "exit" in data :
                break
            time.sleep(1)