# Main File

# Import Library and Modules
from module.bruteforce import run_brute_force_closest_pair
from module.divideconquer import run_divide_and_conquer_closest_pair
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

# Function to display brute force answer on GUI
def display_bf(event):
    run_brute_force_closest_pair(answer, canvas)

# Function to display divide and conquer answer on GUI
def display_dnc(event):
    run_divide_and_conquer_closest_pair(answer, canvas)

# Initializing GUI
window = tk.Tk()
answer = tk.StringVar()

frame = tk.Frame(master=window, width=1280, height=720)
frame.pack()

window.geometry("1280x720")
window.title("Closest Point Pair App")

label1 = tk.Label(master=frame, text="Closest Point Pair", font=("Courier", 24))
label1.pack(padx=50, pady=10)

label2 = tk.Label(master=frame, text="by: Michael Jonathan Halim | 13521124\n    Enrique Alifio Ditya   | 13521142", font=("Courier", 14))
label2.pack(padx=50, pady=10)

buttons = tk.Frame(frame)
buttons.pack(padx=50, pady=10)

button1 = tk.Button(master=buttons, text="Try With Brute Force!")
button1.pack(side=LEFT, padx=10)
button1.bind("<Button-1>", display_bf)

button2 = tk.Button(master=buttons, text="Try With Divide and Conquer!")
button2.pack()
button2.bind("<Button-1>", display_dnc)

label3 = tk.Label(master=frame, textvariable=answer, font=("Courier", 10))
label3.pack(padx=50, pady=10)

canvas = Canvas(frame) 
canvas.pack(padx=50, pady=(0,50))

window.mainloop()