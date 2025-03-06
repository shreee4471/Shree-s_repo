import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import tkinter as tk
from tkinter import messagebox

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def commands():
    """Listens to microphone input and returns recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source)
            print("Processing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You just said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            speak("Sorry, I didn't catch that. Please repeat.")
            return "none"
        except Exception as e:
            print(f"Error: {e}")
            speak("An error occurred. Please try again.")
            return "none"
    return query

def wishings():
    """Greets the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good morning, boss!")
        speak("Good morning, boss!")
    elif 12 <= hour < 17:
        print("Good afternoon, boss!")
        speak("Good afternoon, boss!")
    elif 17 <= hour < 21:
        print("Good evening, boss!")
        speak("Good evening, boss!")
    else:
        print("Good night, boss!")
        speak("Good night, boss!")

def search_youtube():
    """Listens to user's query and searches it on YouTube."""
    print("What should I search on YouTube?")
    speak("What should I search on YouTube?")
    search_query = commands().lower()
    if search_query != "none":
        print(f"Searching YouTube for: {search_query}")
        speak(f"Searching YouTube for {search_query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

def main():
    """Main function to handle user commands."""
    wishings()
    while True:
        query = commands().lower()

        # Exit command
        if "stop" in query or "exit" in query:
            print("Goodbye, boss!")
            speak("Goodbye, boss!")
            break

        # Time command
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {current_time}.")
            speak(f"The time is {current_time}.")

        # Open a website
        elif "open google" in query:
            print("Opening Google...")
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in query:
            print("Opening YouTube...")
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        # Search on YouTube
        elif "search on youtube" in query:
            search_youtube()

        # Play music
        elif "play music" in query:
            music_dir = "C:\\Users\\YourUsername\\Music"  # Replace with your music directory path
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                print(f"Playing {song}...")
                speak(f"Playing {song}.")
                os.startfile(os.path.join(music_dir, song))
            else:
                print("No music files found in the directory.")
                speak("No music files found in the directory.")

        # Open an application
        elif "open notepad" in query:
            print("Opening Notepad...")
            speak("Opening Notepad.")
            os.system("notepad")

        elif "open calculator" in query:
            print("Opening Calculator...")
            speak("Opening Calculator.")
            os.system("calc")

        # Joke command
        elif "tell me a joke" in query:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "What do you call fake spaghetti? An impasta!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!"
            ]
            joke = random.choice(jokes)
            print(f"Here's a joke: {joke}")
            speak(joke)

        # Unknown command
        else:
            print("I didn't understand that command.")
            speak("I didn't understand that command. Please try again.")

if __name__ == "__main__":
    main()
