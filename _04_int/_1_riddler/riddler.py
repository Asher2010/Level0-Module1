"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    correct = 0
    question = simpledialog.askstring(title="Riddle 1", prompt="What 8 letter word can have a letter taken away and it still makes a word. Take another letter away and it still makes a word. Keep on doing that until you have one letter left. What is the word?")
    if question == "Starting":
        print("Correct!")
        correct += 1
    else:
        print("Incorrect")
    question2 = simpledialog.askstring(title="Riddle 2", prompt="The more you take, the more you leave behind. What am I?")
    if question2 == "Footsteps":
        print("Correct!")
        correct += 1
    else:
        print("Incorrect")
    question3 = simpledialog.askstring(title="Riddle 3", prompt="David's father has three sons: Snap, Crackle, and _____?")
    if question3 == "David":
        print("Correct!")
        correct += 1
    else:
        print("Incorrect")

    print(correct)
