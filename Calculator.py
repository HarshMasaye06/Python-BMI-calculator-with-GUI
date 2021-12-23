from tkinter import *

root = Tk()
root.title("BMI calculator")


# deletes the content form height field when clicked
def click1(event):
    e1.config(state=NORMAL)
    e1.delete(0, END)


# deletes the content form weight field when clicked
def click2(event):
    e2.config(state=NORMAL)
    e2.delete(0, END)


# entry box to take weigth input
e1 = Entry(root, width=15, borderwidth=5, text="enter your weight")
e1.config(state=NORMAL)
e1.delete(0, END)
e1.insert(0, "Weight in kg")
e1.config(state=DISABLED)
e1.bind("<Button-1>", click1)
e1.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

# entry box to take heigth input
e2 = Entry(root, width=15, borderwidth=5, text="enter your height")
e2.config(state=NORMAL)
e2.delete(0, END)
e2.insert(0, "Height in feet")
e2.config(state=DISABLED)
e2.bind("<Button-1>", click2)
e2.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# shows the result
e3 = Entry(root, width=40, borderwidth=5)
e3.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# shows info chart about distributions and where they lie on bmi scale
e4 = Label(root, text="16.5<--------->18.5<---------->25.0<---------->40.0")
e4.grid(row=2, columnspan=4)
e5 = Label(root, text="Underweight", fg='blue')
e5.grid(row=3, column=0)
e6 = Label(root, text="Normal", fg='green')
e6.grid(row=3, column=1)
e7 = Label(root, text="Overweight", fg='red')
e7.grid(row=3, column=2)


def button_cal(number):
    current1 = e1.get()
    e1.delete(0, END)
    e1.insert(0, str(current1) + str(number))

    current2 = e2.get()
    e2.delete(0, END)
    e2.insert(0, str(current2) + str(number))


def button_equal():
    weight = e1.get()
    global w_inp
    w_inp = float(weight)

    height = float(e2.get()) / 3.3048
    global h_inp
    h_inp = float(height)
    # bmi formula (weight / height ** 2)
    e3.insert(0, w_inp / h_inp ** 2)




def button_clear():
    # e1.delete(0, END)
    # e2.delete(0, END)
    e3.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_cal(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_cal(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_cal(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_cal(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_cal(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_cal(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_cal(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_cal(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_cal(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_cal(0))
button_equal = Button(root, text="=", padx=40, pady=20, bg='#ff9600', command=button_equal)
button_clear = Button(root, text="Clear", padx=30, pady=20, command=button_clear)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)

button_7.grid(row=6, column=0)
button_8.grid(row=6, column=1)
button_9.grid(row=6, column=2)

button_0.grid(row=7, column=1)
button_equal.grid(row=7, column=2)
button_clear.grid(row=7, column=0)
root.mainloop()
