import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import numpy as np

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Boss!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")

    speak("I am EDITH. Please tell me how may I help you!")
    

def takeCommand():
    # It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_address', 'your_password')
    server.sendmail('your_email_address', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

         # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
    
        elif 'open coursera' in query:
            webbrowser.open("coursera.org")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play movies' in query:
            movie_dir = 'C:\\Users\\Vardhan\\Desktop\\MOVIES'
            movies = os.listdir(movie_dir)
            print(movies)
            
            os.startfile(os.path.join(movie_dir, songs[0]))




        elif 'open jupyter' in query:
            codePath = "C:\\Users\\Vardhan\\Anaconda3\\python.exe C:\\Users\\Vardhan\\Anaconda3\\cwp.py C:\\Users\\Vardhan\\Anaconda3 C:\\Users\\Vardhan\\Anaconda3\\python.exe C:\\Users\\Vardhan\\Anaconda3\\Scripts\\jupyter-notebook-script.py '%USERPROFILE%/'"
            os.startfile(codePath)

        elif 'open gaana' in query:
            webbrowser.open("gaana.com")
    
        elif 'open googlecolab' in query:
            webbrowser.open("googlecolab.com")

        elif 'email to vardhan' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "your_email_address"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss,  I am not able to send this email")
                