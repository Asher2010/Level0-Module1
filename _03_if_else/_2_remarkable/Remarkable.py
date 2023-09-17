from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(title="name", prompt = "Enter a name")
    if name == "Luke":
        print("Sucks at all games")
    if name == "Karina":
        print("Likes drawing")
    if name == "Ashwin":
        print("Good at soccer")

