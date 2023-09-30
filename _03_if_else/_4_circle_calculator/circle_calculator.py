import math
from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # Write a Python program that asks the user for the radius of a circle.
    radius = simpledialog.askinteger(title="Radius", prompt="Enter a radius")
    # Next, ask the user if they would like to calculate the area or circumference of a circle.
    question = simpledialog.askstring(title="Area or Circumference", prompt="Calculate the area or circumference?")
    # If they choose area, display the area of the circle using the radius.
    if question == "area":
        Area = math.pi*radius*radius
        print(Area)
    # Otherwise, display the circumference of the circle using the radius.
    else:
        Circumference = 2*math.pi*radius
        print(Circumference)

