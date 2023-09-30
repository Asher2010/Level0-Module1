import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    turty = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    question = simpledialog.askstring(title="Shape", prompt="What shape would you like to draw?(triangle, square, or circle)")
    # Draw the shape requested by the user using if-elif-else statements
    if question == "circle":
        turty.circle(200, 400, 100)
    elif question == "square":
        turty.pendown()
        turty.forward(200)
        turty.left(90)
        turty.forward(200)
        turty.left(90)
        turty.forward(200)
        turty.left(90)
        turty.forward(200)

    elif question == "triangle":
        turty.forward(200)
        turty.left(120)
        turty.forward(200)
        turty.left(120)
        turty.forward(200)

    # Call the turtle .done() method
    turtle.done()
