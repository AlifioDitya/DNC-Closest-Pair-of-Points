# Main File

# Import Library and Modules
from module.bruteforce import run_brute_force_closest_pair
from module.divideconquer import run_divide_and_conquer_closest_pair
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random
from module.Point import Point

# Function to generate points
def generate_points(n, dimension):
    # Generate random data
    coordinates = []
    for _ in range (dimension):
        temp_coordinate = [random.randint(1, n) for _ in range(n)]
        coordinates.append(temp_coordinate)

    # Pack the data into Point objects
    points = []
    for i in range (n):
        temp = []
        for j in range (dimension):
            temp.append(coordinates[j][i])
        temp_point = Point(*temp)
        points.append(temp_point)

    return points

# Function to display solution on GUI
def display_solution(event):
    if(input_n.get() != "" and input_dimension.get() != ""):
        n = int(input_n.get())
        dimension = int(input_dimension.get())
        if(n <= 1 or dimension <= 0):
            mb.showerror(title="Error", message="Input not valid. N must be greater than 1 and Dimension must be greater than 0.")
        else:
            titlebf.set("Brute Force")
            titlednc.set("Divide and Conquer")
            points = generate_points(n, dimension)
            if(dimension <= 3):
                run_brute_force_closest_pair(points, answer1, canvas, True)
                run_divide_and_conquer_closest_pair(points, answer2)
            else:
                run_brute_force_closest_pair(points, answer1, canvas, False)
                run_divide_and_conquer_closest_pair(points, answer2)
    else:
        mb.showerror(title="Error", message="Don't forget to input N and dimension.")

# Initializing GUI
window = tk.Tk()
answer1 = tk.StringVar()
answer2 = tk.StringVar()
titlebf = tk.StringVar()
titlednc = tk.StringVar()

window.configure(background='#1C1C1C')

window.geometry("1280x720")
window.title("Closest Pair of Points App")

label1 = tk.Label(master=window, text="Closest Pair of Points", font=("Helvetica", 24, 'bold'), background='#1C1C1C', foreground="white")
label1.pack(padx=50)

label2 = tk.Label(master=window, text="by: Michael Jonathan Halim | 13521124\n      Enrique Alifio Ditya         | 13521142", font=("Helvetica", 14), background='#1C1C1C', foreground="white")
label2.pack(padx=50)

inputs = tk.Frame(window, background='#1C1C1C')
inputs.pack(padx=50)

firstInput = tk.Frame(inputs, background='#1C1C1C')
firstInput.pack(pady=10, anchor="w")

label_input_n = tk.Label(master=firstInput, text="N (number of points)  = ", font=("Helvetica", 10), background='#1C1C1C', foreground="white")
label_input_n.pack(side=LEFT)
input_n = Entry(firstInput, width = 20)
input_n.focus_set()
input_n.pack()

secondInput = tk.Frame(inputs, background='#1C1C1C')
secondInput.pack(anchor="w")

label_input_dimension = tk.Label(master=secondInput, text="Dimension                 = ", font=("Helvetica", 10), background='#1C1C1C', foreground="white")
label_input_dimension.pack(side=LEFT)
input_dimension = Entry(secondInput, width = 20)
input_dimension.focus_set()
input_dimension.pack()

buttons = tk.Frame(window, background='#1C1C1C')
buttons.pack(padx=50, pady=10)

button1 = tk.Button(master=buttons, text="Calculate", bg='#1C1C1C', fg="white")
button1.pack(side=LEFT, padx=10)
button1.bind("<Button-1>", display_solution)

answers = tk.Frame(window, background='#1C1C1C')
answers.pack(padx=50)

bflabel = tk.Frame(answers, background='#1C1C1C')
bflabel.pack(side=LEFT, padx=20)

dnclabel = tk.Frame(answers, background='#1C1C1C')
dnclabel.pack()

subtitle1 = tk.Label(master=bflabel, textvariable=titlebf, font=("Helvetica", 15), background='#1C1C1C', foreground="white")
subtitle1.pack()

label3 = tk.Label(master=bflabel, textvariable=answer1, font=("Comic Sans MS", 10), background='#1C1C1C', foreground="white")
label3.pack()

subtitle2 = tk.Label(master=dnclabel, textvariable=titlednc, font=("Helvetica", 15), background='#1C1C1C', foreground="white")
subtitle2.pack()

label4 = tk.Label(master=dnclabel, textvariable=answer2, font=("Comic Sans MS", 10), background='#1C1C1C', foreground="white")
label4.pack()

canvas = Canvas(window, background='#1C1C1C', bd=0, highlightthickness=0, relief='ridge') 
canvas.pack(padx=50, pady=(0,10))

window.mainloop()