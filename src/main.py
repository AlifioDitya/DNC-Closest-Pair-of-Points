# Main File

# Import Library and Modules
from module.Point import Point
import matplotlib.pyplot as plt
from module import bruteforce as bf
import tkinter as tk
from tkinter import *

# Function to display brute force answer on GUI
def display_bf(event):
    bf.run_brute_force_closest_pair(answer)

# Initializing GUI
window = tk.Tk()
answer = tk.StringVar()

frame = tk.Frame(master=window, width=800, height=400)
frame.pack()

window.geometry("800x400")
window.title("Closest Point Pair App")

label1 = tk.Label(master=frame, text="Closest Point Pair", font=("Courier", 24))
label1.pack(padx=50, pady=10)

label2 = tk.Label(master=frame, text="by: Michael Jonathan Halim | 13521124\n    Enrique Alifio Ditya   | 13521142", font=("Courier", 14))
label2.pack(padx=50, pady=10)

button1 = tk.Button(master=frame, text="Try With Brute Force!")
button1.pack(padx=50, pady=10)

button1.bind("<Button-1>", display_bf)

label3 = tk.Label(master=frame, textvariable=answer, font=("Courier", 10))
label3.pack(padx=50, pady=10)

window.mainloop()