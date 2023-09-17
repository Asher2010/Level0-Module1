from tkinter import messagebox, simpledialog, Tk
import datetime
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    today = str(month)+"/"+str(day)
    question = simpledialog.askstring(title = "Birthday", prompt = "When is your birthday?")
    if question == today:
        print("Happy Birthday")
    else:
        print("Happy Unbirthday")

