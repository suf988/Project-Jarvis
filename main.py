import speech_recognition as sr
import webbrowser
import pyttsx3
from musicLibrary import music
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsApiKey = "enter-your-own-news-api-key"
openAiApiKey = "enter-your-own-open-ai-api-key" # Open AI api is paid

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
        song = c.split(" ",1)[1]
        link = music.get(song)
        if link:
            webbrowser.open(link)
        else:
            available_songs = ", ".join(music.keys())
            speak(f"Sorry, I don't have {song} song in my playlist. The songs I have are {available_songs}")
    
    # tell the news:
    elif 'news' in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApiKey}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])
            titles = [article['title'] for article in articles]

            for title in titles:
                speak(title)
    
    # acts as an AI assistant:
    else:
        client = OpenAI(api_key=openAiApiKey)
        completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant named Jarvis, like Alexa and Google Cloud"},
                {"role": "user", "content": c}
            ]
        )
        speak(completion.choices[0].message)

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