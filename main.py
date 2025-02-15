import speech_recognition as sr
import webbrowser
import pyttsx3
from musicLibrary import music
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsApiKey = "f513b66ee0364db5a3593ad4f0866664"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):

    # open web pages:
    if 'open google' in c:
        webbrowser.open('https://google.com')
    elif 'open facebook' in c:
        webbrowser.open('https://facebook.com')
    elif 'open youtube' in c:
        webbrowser.open('https://youtube.com')
    elif 'open linkedin' in c:
        webbrowser.open('https://linkedin.com')
    
    # play music:
    elif c.startswith('play'):
        song = c.split(' ')[1]
        link = music[song]
        webbrowser.open(link)
    
    # tell the news:
    elif 'news' in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApiKey}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])
            titles = [article['title'] for article in articles]

            for title in titles:
                speak(title)

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