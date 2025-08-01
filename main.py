import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
import os
from openai import OpenAI
from gtts import gTTS

#pip install pocketsphinx

recoginzier = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "#"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')


    # Initialize pygame mixer
    pygame.mixer.init()

    # Load your MP3 file
    pygame.mixer.music.load("temp.mp3")  # Replace with your actual file name

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running while music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Wait to let music play

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(
    api_key="#",
    ) 

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa or Google Assistant. Give short responses please"},
        {"role": "user", "content": command }
    ]
    )

    return(completion.choices[0].message.content)




def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            #Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        #let OpenAI handle the request
        output = aiProcess(c)
        speak(output)




    


if __name__ == "__main__":
    speak("initializing Jarvis....")
    while True:
        #Listen for the wake word Jarvis 
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recoginizing..")
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout = 5,phrase_time_limit= 4)
            word = r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("ya")
                # #listen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

   
