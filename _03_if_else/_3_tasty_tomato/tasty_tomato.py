from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':

    window_width = 600
    window_height = 600

    root = tk.Tk()

    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
    canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
    color = simpledialog.askstring(title="Color", prompt = "Enter a color")

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
    if color == "red":
        canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    if color == "green":
        canvas.create_oval(200, 200, 525, 450, fill="green", outline="")
    if color == "purple":
        canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
    if color == "pink":
        canvas.create_oval(200, 200, 525, 450, fill="pink", outline="")
    if color == "orange":
        canvas.create_oval(200, 200, 525, 450, fill="orange", outline="")
    if color == "yellow":
        canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
    if color == "black":
        canvas.create_oval(200, 200, 525, 450, fill="black", outline="")
    if color == "white":
        canvas.create_oval(200, 200, 525, 450, fill="white", outline="")
    if color == "blue":
        canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
    if color == "brown":
        canvas.create_oval(200, 200, 525, 450, fill="brown", outline="")
    if color == "grey":
        canvas.create_oval(200, 200, 525, 450, fill="grey", outline="")
    canvas.create_rectangle(375, 100, 325, 230, fill="green", outline="")

    root.mainloop()
