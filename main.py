import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "John"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    #speak("How may I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = recognize_google(audio, language = 'en-GB')
        print(f"Usear said: {query}\n")
    except Exception as e:
        print("Say that again, please")
        query = None
    return query

def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('harry@harry.com', to , content)
    server.close()

def main():
    speak("Initalizing Jarvis...")
    WishMe()
    query = TakeCommand()

    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        webbrowser.open('youtube.com')
    #speak("Hi. I'm Jarvis. What is your name?")

    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

main()