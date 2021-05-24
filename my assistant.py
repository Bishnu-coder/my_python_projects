import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
from googlesearch import search
from tkinter import *

root = Tk()
root.geometry('600x400')



print("Hello sir I am your assistant\n How can I help you?")

hour = (datetime.datetime.now().hour)

if hour>=6 and hour<12:
    pyttsx3.speak("good morning")
    l1=Label(text="Good morning",bg="grey",fg="black")
    l1.pack(anchor=NW)
elif hour>=12 and hour<18:
    pyttsx3.speak("good afternoon")
    l1=Label(text="Good afternoon",bg="grey",fg="black")
    l1.pack(anchor=NW)
else:
    pyttsx3.speak("good evening")
    l1=Label(text="Good evening",bg="grey",fg="black")
    l1.pack(anchor=NW)

min = (datetime.datetime.now().minute)
date1 =(datetime.datetime.now().year)
date2 =(datetime.datetime.now().month)
date3=(datetime.datetime.now().day)
engine = pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.say("hello i am your assistant JARVIS How can i help you")
l1=Label(text="Hello i am your assistant\n JARVIS How can i help you",bg="grey",fg="black")
l1.pack(anchor=NW)
engine.runAndWait()

try:
    while (True):
        print("listening.....")
        l1=Label(text="listening.....",bg="grey",fg="black")
        l1.pack(anchor=NW)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)                  
        query = r.recognize_google(audio, language='en-in') 
        print("User said:"+query)
        l1=Label(text="user said"+query,bg="grey",fg="black")
        l1.pack(anchor=NW)
        if "close" in query:
            pyttsx3.speak("closing")
            break
        elif"how are you"in query:
            engine.say("i am fine! and you sir")
            engine.runAndWait()
        elif"time"in query:
            pyttsx3.speak(hour) 
            pyttsx3.speak(min)
        elif"date"in query: 
            pyttsx3.speak(date1)
            pyttsx3.speak(date2)
            pyttsx3.speak(date3)
        elif "YouTube"in query:
            pyttsx3.speak("opening youtube")
            for j in search("youtube.com",num=1, stop=1, pause=2):
                webbrowser.open(j)
        elif "Google"in query:
            pyttsx3.speak("opening google")
            for j in search("google.com",num=1, stop=1, pause=2):
                webbrowser.open(j)
        elif 'open vs code' in query:
            pyttsx3.speak("opening vs code")            
            codePath = "C:\\Users\\SIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "downloads"in query:
            pyttsx3.speak("opening downloads")
            codePath = "C:\\Users\\SIT\\Downloads"
            os .startfile(codePath)
        elif "CMD"in query:
            pyttsx3.speak("opening cmd")
            codePath = "C:\\Users\\SIT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
            os .startfile(codePath)
        elif "Chrome"in query:
            pyttsx3.speak("opening crome")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome..exe"
            os .startfile(codePath)
        elif "disk d"in query:
            pyttsx3.speak("opening local disk d")
            os.startfile("d:")
        elif "disk c"in query:
            pyttsx3.speak("opening local disk c")
            os.startfile("c:")
        elif "disk e"in query:
            pyttsx3.speak("opening local disk e")
            os.startfile("e:")
        elif "pictures"in query:
            pyttsx3.speak("opening pictures")
            os.startfile("c:\\users\\sit\\pictures")
        elif "videos"in query:
            pyttsx3.speak("opening videos")
            os.startfile("c:\\users\\sit\\videos")
        elif "documents"in query:
            pyttsx3.speak("opening documents")
            os.startfile("c:\\users\\sit\\documents")
        elif "music"in query:
            pyttsx3.speak("opening music")
            os.startfile("c:\\users\\sit\\music")
        elif "made you"in query:
            pyttsx3.speak("bishnu parjapati made me")
        elif "codes"in query:
            pyttsx3.speak("opening codes")
            os.startfile("C:\\Users\\SIT\\Videos\\codes")
        elif "script"in query:
            pyttsx3.speak("opening scripts")
            os.startfile("C:\\Users\\SIT\\Python\\Scripts")
        elif "who are you"in query:
            pyttsx3.speak("i am your assistant my name is jarvis")
except Exception as e:
    pyttsx3.speak("I am turning off")



root.mainloop()

    
   






