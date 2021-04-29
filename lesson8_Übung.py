import tkinter
from tkinter import ttk

result = 0

window = tkinter.Tk()

hello_label = tkinter.Label(window, text="Please choose type of conversion and enter number:")
hello_label.pack()
conv = ttk.Combobox(window, values=["Fahrenheit to Celsius", "Cup to Milliliter", "Pounds to Grams"])
conv.pack()
number = tkinter.Entry(window)
number.pack()
res_label = tkinter.Label(window, text=result)
res_label.pack()


def button_click():
    if conv.get() == "Fahrenheit to Celsius":
        result = (int(number.get()) - 32)/1.8
    elif conv.get() == "Cup to Milliliter":
        result = int(number.get()) * 250
    elif conv.get() == "Pounds to Grams":
        result = int(number.get()) * 453.592
    result_str = "{:,.2f}".format(result)
    res_label.config(text=result_str)


submit = tkinter.Button(window, text="Convert!", command=button_click)
submit.pack()

window.mainloop()
