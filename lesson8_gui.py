import tkinter
import random
from tkinter import messagebox

secret = random.randint(1, 20)
window = tkinter.Tk()

hello_label = tkinter.Label(window, text="Guess the number")
hello_label.pack()
guess = tkinter.Entry(window)
guess.pack()

def button_click():
    if int(guess.get()) == secret:
        result_text = "You won!"
    elif int(guess.get()) > secret:
        result_text = "Wrong, number is too high."
    else:
        result_text = "Wrong, number is too low."
    messagebox.showinfo("Result:", result_text)

submit = tkinter.Button(window, text="Submit", command=button_click)
submit.pack()

window.mainloop() # damit das window konstant angezeigt wird und nicht sofort wieder verschwindet

#Übung: GUI für eines der entwickelten Programme (z.B. Unit Converter) programmieren
