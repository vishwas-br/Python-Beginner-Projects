from tkinter import *

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("500x300")


def calculate():
    prin = float(principalentry.get())
    rat = float(rateentry.get())
    tim = float(timeentry.get())
    amount = (prin*rat*tim)/100
    Label(text=f"{amount}", font="arial 30 bold").place(x=200, y=220)


principal = Label(root, text="Principal:", font="arial 15")
rate = Label(root, text="Rate of Interest:", font="arial 15")
time = Label(root, text="Time(in years):", font="arial 15")
interest = Label(root, text="Interest:", font="arial 15")
interest.place(x=50, y=230)
principal.place(x=50, y=20)
rate.place(x=50, y=90)
time.place(x=50, y=160)

principalvalue = StringVar()
ratevalue = StringVar()
timevalue = StringVar()

principalentry = Entry(root, textvariable=principalvalue, font="arial 20", width=8)
rateentry = Entry(root, textvariable=ratevalue, font="arial 20", width=8)
timeentry = Entry(root, textvariable=timevalue, font="arial 20", width=8)

principalentry.place(x=200, y=20)
rateentry.place(x=200, y=90)
timeentry.place(x=200, y=160)

Button(text="Calculate", font="arial 15", command=calculate).place(x=350, y=20)
Button(root, text="Exit", command=lambda: exit(), font="arial 15", width=8).place(x=350, y=90)
root.mainloop()
