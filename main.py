import speech_recognition as sr
import webbrowser
import pyttsx3
from musicLibrary import music

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if 'open google' in c:
        webbrowser.open('https://google.com')
    elif 'open facebook' in c:
        webbrowser.open('https://facebook.com')
    elif 'open youtube' in c:
        webbrowser.open('https://youtube.com')
    elif 'open linkedin' in c:
        webbrowser.open('https://linkedin.com')
    elif c.startswith('play'):
        song = c.split(' ')[1]
        link = music[song]
        webbrowser.open(link)


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        # listening for the wake word "Jarvis" by obtaining audio from microphone:
        try:
            with sr.Microphone() as source:

                print("Listening.....\n")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            print("Recognizing..... \n")
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                print("Jarvis Active\n")
                speak("Yeah I am listening")

                # listen for command:
                with sr.Microphone() as source:
                    print("Listening command\n")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
                command = recognizer.recognize_google(audio).lower()

                processCommand(command)

        except Exception as e:
            print(f"Error: {e}\n")