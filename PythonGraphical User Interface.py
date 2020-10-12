#import tkinter as tk
from tkinter import * #you don't have to use tk.Tk() if you import *
def checking():
    my_name = "Hello World!"
    mytextbox.insert(0, my_name)
    return None

odwa = Tk()
odwa.title("GRAPHICAL USER INTERFACE")
odwa.geometry("400x300")
odwa.configure(background="black")

mrLabel= Label(odwa, text="Hello to Everyone", relief="solid") #give it any name & relief will give you sort of border
mrLabel.pack()

mytextbox = Entry(odwa, width=20)
mytextbox.pack()

my_button = Button(odwa, text="Click me!", bg="red", command=checking)#by command you always put your function name without brackets
my_button.pack()

odwa.mainloop()