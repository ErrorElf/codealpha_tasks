import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():  
        engine.setProperty('voice', voice.id)
        break
else:
    print("No female voice found! Using default voice.")
engine.setProperty('rate', 170)  


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return None
        except sr.RequestError:
            speak("There seems to be a problem with the speech recognition service.")
            return None
        except sr.WaitTimeoutError:
            speak("You took too long to respond.")
            return None


def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am June, your voice assistant. How can I help you today?")


def execute_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad.exe")
    elif "exit" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("Sorry, I didn't understand that. Could you try again?")


def main():
    greet_user()
    while True:
        command = listen()
        if command:
            execute_command(command)


if __name__ == "__main__":
    main()
