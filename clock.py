from tkinter import *
from time import strftime, strptime
import pyttsx3




root=Tk()
root.geometry("300x100")
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


root.mainloop()
