import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from datetime import datetime

recognizer = sr.Recognizer()

def speak(text):
    print(f"Ultron: {text}")
    # Re-initialize engine each time to avoid silent bug
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # or voices[1].id if you prefer Zira
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("I can't hear you master.")
            return ""
        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

def main():
    speak("I am ultron what's your command master Ankit.")
    while True:
        command = listen()
        print("DEBUG: Command received ->", command)

        if "hello" in command:
            speak("Hi master how's your day going.")
        elif "time" in command:
            now = datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")
        elif "youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open_new_tab("https://www.youtube.com")
        elif "google" in command:
            speak("Opening Google.")
            webbrowser.open_new_tab("https://www.google.com")
        elif "song" in command or "play song" in command:
            speak("Playing Song on YouTube.")
            webbrowser.open_new_tab("https://youtu.be/xw4ko4WuI0Y?si=VKGbOZMJDNy_8Yni")
        elif "notepad" in command:
            speak("Opening Notepad.")
            os.system("notepad")
        elif "calculator" in command:
            speak("Opening Calculator.")
            os.system("calc")
        elif "exit" in command or "quit" in command:
            speak("Shutting down. Goodbye.")
            break
        else:
            if command:
                speak("I don't know.")

if __name__ == "__main__":
    main()