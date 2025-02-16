# Jarvis - Voice-Activated Virtual Assistant

Jarvis is a voice-controlled virtual assistant built to handle tasks like browsing the web, playing music, retrieving news, and answering user questions using OpenAI's GPT-4o-mini model.

## Features

- **Voice Recognition**: Uses `speech_recognition` to listen for and recognize voice commands. Activates upon detecting the wake word `Jarvis`.
- **Text-to-Speech**: Converts text to speech and plays it using `pyttsx3`.
- **Web Browsing**: Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice commands.
- **Music Playback**: Plays songs using links stored in `musicLibrary.py`.
- **News Fetching**: Fetches and reads the latest news headlines using the `NewsAPI`.
- **OpenAI Integration**: Handles complex queries using OpenAI's GPT-4o-mini and acts as a general virtual assistant.

## Workflow

- **Initialization**: Greets the user with `Initializing Jarvis....`.
- **Wake Word Detection**: Listens for the wake word `Jarvis`.
- **Acknowledges Actication**: Responds to the wake word by saying `Yeah I am listening`.
- **Command Processing**: Processes commands to determine actions such as opening a website, playing music, fetching news, or generating a response via OpenAI.
- **Speech Output**: Provides responses using speak function with `pyttsx3`.

## Libraries Used:

- speech_recognition
- webbrowser
- pyttsx3
- requests
- openai
- pyaudio

## Installation

To set up the project, clone this repository and install the required dependencies using:

pip install -r requirements.txt


## Usage

Run the script to start Jarvis and give voice commands to interact with it. You can ask Jarvis to open websites, play music, fetch news, and more.
