import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os,random,subprocess
import random
import smtplib
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Kushal Sir')

    if hour>=12 and hour<17:
        speak('Good Afternoon Kushal Sir')

    if hour>=17 and hour<20:
        speak('Good evening Kushal Sir')

    if hour>=20 and hour<=23:
        speak('Good evening Kushal Sir')

    speak("Hello I am Spidy a Virtual assistant, How can i Help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print('I am Listening......')
        audio = r.listen(source)

    try:
        print('Recognising.....Please wait......')
        query = r.recognize_google(audio,language='en-in')
        print("You said:",query)
    except Exception as e:
        print('Say that again please....')
        return "None"
    return query

if __name__ == "__main__":
    print("Hello i am Spidy a virtual assistant who developed by Kushal Bhavsar")
    wishme()

    while True:
        query = takecommand().lower()

        if 'stop' in query:
            speak('Good bye sir')
            break

        if 'wikipedia' in query:
            print('Searching for you in wikipedia')
            speak('Searching for you in wikipedia')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=1)
            print(result)
            speak(result)

        elif 'your name' in query:
            print('My name is spidy ! I am virtual assistant of Kushal Bhavsar')
            speak('My name is spidy I am virtual assistant of Kushal Bhavsar')

        elif 'open youtube' in query:
            web = 'www.youtube.com'
            wb = 'C:/Program Files/Mozilla Firefox/firefox.exe'
            speak('opening youtube for you')
            subprocess.call([wb,web])


        elif 'open stackoverflow' in query:
            web = 'wwww.stackoverflow.com'
            speak('opening stackoverflow for you')
            wb = 'C:/Program Files/Mozilla Firefox/firefox.exe'
            speak('opening stackoverflow for you')
            subprocess.call([wb,webbrowser])

        elif 'song' in query:
            mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
            randomfile = random.choice(os.listdir("E:/kushal choice/"))
            file = ('E:/kushal choice/' + randomfile)
            print('Playing : '+ randomfile+ ' for you')
            subprocess.call([mp,file])

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print('Current time is:' ,strtime)
            speak(f"Current time is{strtime}")

        elif 'google' in query:
            query = query.replace('google', '')
            ur = "https://www.google.com/search?source=hp&ei=-8_PXI-EB4WcmgeU3YLwCg&q="
            webbrowser.open_new(ur + query)