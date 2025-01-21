import tkinter
from tkinter import *

def add_digit(digit):
    value = entry.get()
    if value[0]=='0' and len (value)==1:
        value = value[1:]
    entry.delete(0, tkinter.END)
    entry.insert(0, value + digit)

def add_operation(operation) :
    value = entry.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value :
        calculate()
        value = entry.get()
    entry.delete(0, tkinter.END)
    entry.insert(0, value + operation)

def calculate():
    value = entry.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    entry.delete(0, tkinter.END)
    entry.insert(0, eval(value))

def clear():
    entry.delete(0, tkinter.END)
    entry.insert(0,0)

window = tkinter.Tk()
window.title('Калькулятор')
window.geometry('250x250')

entry = tkinter.Entry(window, justify=tkinter.RIGHT, font=('',15),width=15)
entry.insert(0,'0')
entry.place(x=10, y=10)
entry.grid(row=0, column=0, columnspan=3, padx=5)

#кнопки и их расположение в окне
tkinter.Button(text='1', bd=5, command=lambda : add_digit('1')).grid(row=1, column=0,stick='wens',padx=5,pady=5)
tkinter.Button(text='2', bd=5, command=lambda : add_digit('2')).grid(row=1, column=1,stick='wens',padx=5,pady=5)
tkinter.Button(text='3', bd=5, command=lambda : add_digit('3')).grid(row=1, column=2,stick='wens',padx=5,pady=5)
tkinter.Button(text='4', bd=5, command=lambda : add_digit('4')).grid(row=2, column=0,stick='wens',padx=5,pady=5)
tkinter.Button(text='5', bd=5, command=lambda : add_digit('5')).grid(row=2, column=1,stick='wens',padx=5,pady=5)
tkinter.Button(text='6', bd=5, command=lambda : add_digit('6')).grid(row=2, column=2,stick='wens',padx=5,pady=5)
tkinter.Button(text='7', bd=5, command=lambda : add_digit('7')).grid(row=3, column=0,stick='wens',padx=5,pady=5)
tkinter.Button(text='8', bd=5, command=lambda : add_digit('8')).grid(row=3, column=1,stick='wens',padx=5,pady=5)
tkinter.Button(text='9', bd=5, command=lambda : add_digit('9')).grid(row=3, column=2,stick='wens',padx=5,pady=5)
tkinter.Button(text='0', bd=5, command=lambda : add_digit('0')).grid(row=4, column=0,stick='wens',padx=5,pady=5)

tkinter.Button(text='+', bd=5, command=lambda : add_operation('+')).grid(row=1, column=3,stick='wens',padx=5,pady=5)
tkinter.Button(text='-', bd=5, command=lambda : add_operation('-')).grid(row=2, column=3,stick='wens',padx=5,pady=5)
tkinter.Button(text='/', bd=5, command=lambda : add_operation('/')).grid(row=3, column=3,stick='wens',padx=5,pady=5)
tkinter.Button(text='*', bd=5, command=lambda : add_operation('*')).grid(row=4, column=3,stick='wens',padx=5,pady=5)

tkinter.Button(text='=', bd=5, command=calculate).grid(row=4, column=1,stick='wens',padx=5,pady=5)
tkinter.Button(text='C ', bd=5, command=clear).grid(row=4, column=2,stick='wens',padx=5,pady=5)

window.grid_columnconfigure (0, minsize=60)
window.grid_columnconfigure (1, minsize=60)
window.grid_columnconfigure (2, minsize=60)
window.grid_columnconfigure (3, minsize=60)

window.mainloop()