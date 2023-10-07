"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
import math
from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    Number = simpledialog.askinteger(title="Number 1", prompt="Enter a number")
    Number2 = simpledialog.askinteger(title="Number 2", prompt="Enter a number")
    print(Number+Number2)
