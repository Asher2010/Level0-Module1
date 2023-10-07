"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
import math
from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    Number1 = simpledialog.askinteger(title="Number 1", prompt="Enter a number")
    Number2 = simpledialog.askinteger(title="Number 2", prompt="Enter a number")
    question1 = simpledialog.askstring(title="Operation", prompt="Would you like to add, subtract, divide, or multiply these numbers?")

    if question1 == "add":
        print(Number1+Number2)
    elif question1 == "Add":
        print(Number1+Number2)
    elif question1 == "subtract":
        print(Number1-Number2)
    elif question1 == "Subtract":
        print(Number1-Number2)
    elif question1 == "multiply":
        print(Number1*Number2)
    elif question1 == "Multiply":
        print(Number1*Number2)
    elif question1 == "divide":
        print(Number1/Number2)
    elif question1 == "Divide":
        print(Number1/Number2)

