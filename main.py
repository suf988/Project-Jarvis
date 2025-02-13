import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        # listening for the wake word "Jarvis" by obtaining audio from microphone
        try:
            with sr.Microphone() as source:

                print("Listening.....\n")

                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)

            print("Recognizing..... \n")
            command = recognizer.recognize_google(audio)
            print(f"{command}\n")

        except Exception as e:
            print(f"Error: {e}")