from tkinter import *
from time import strftime, strptime
import pyttsx3
from pyttsx3 import speak


root=Tk()
root.geometry("400x125")
root.title("speaking clock")
root.minsize(400,125)
root.maxsize(400,125)


def time():
    string = strftime('%I:%M:%S %p')
    l1.config(text=string)
    l1.after(1000,time)
    
l1 = Label(font=("ds-DIGITAL",55),bg="black",fg="green",relief="sunken",borderwidth=2.5)
l1.pack(fill=X,pady=10)
time()

def run():
    speak("The time is")
    speak(strftime('%I%M%p'))

b1=Button(root,command= run,text="speak time",bg="black",fg="green")
b1.pack(fill=X)

root.mainloop()
