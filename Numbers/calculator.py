from tkinter import *
import math

# for clearign entry field and inserting new values
def insert_answer(entry, to_enter):
    # clears entry field of stuff
    entry.delete(0, END)
    # puts in value into entry field
    entry.insert(0, to_enter)

# creating button click functionality
def click(button):
    # takes the value that is in the entry field
    ex = entry.get()
    print(button)
    if ex == 'Invalid: Not a number':
        insert_answer(entry, "")

    match (button):
        case 'C':
            ex = ex[0:len(ex)-1]
            insert_answer(entry, ex)
        case 'CE':
            entry.delete(0, END)
        case '√':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.sqrt(ex))
        case 'pi':
            insert_answer(entry, math.pi)
        case '2pi':
            insert_answer(entry, 2 * math.pi)
        case 'e':
            insert_answer(entry, 2 * math.e)
        case 'x!':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.factorial(ex))
        case 'cos':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.cos(math.radians(ex)))
        case 'tan':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.tan(math.radians(ex)))
        case 'sin':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.sin(math.radians(ex)))
        case 'cosh':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.cosh(math.radians(ex)))
        case 'tanh':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.tanh(math.radians(ex)))
        case 'sinh':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.sinh(math.radians(ex)))
        case '∛':
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.cbrt(ex))
        case "x\u02b8":
                entry.insert(len(ex), "**")
        case "x\u00B3":
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, ex ** 3)
        case "x\u00B2":
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, ex ** 2)
        case "ln":
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.log2(ex))
        case "log10":
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.log10(ex))
        case "deg":
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.degrees(ex))
        case "rad":
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, math.radians(ex))
        case "+" | "-" | "x" | "÷" | "1"| '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' |"(" | ")":
            entry.insert(len(ex), f"{button}")
        case "%":
            try:
                ex = eval(ex)
            except ValueError:
                insert_answer(entry, "Invalid: Not a number")
            else:
                insert_answer(entry, ex/100)
        case '=':
            insert_answer(entry, eval(ex))
        case _ :
            pass

# create GUI window
root = Tk()

# set GUI attributes
root.title("Scientific calculator")
root.config(bg="#793C5C")
# set dimension of window - (width)x(height)+(dist from x)+(dist from y)
root.geometry('680x486+800+100')

# add entry fields - pass in GUI into entry constructor
entry = Entry(root, font=('Comic Sans MS', 20, 'bold'), bg='white', fg='black', bd = 10, width=30)

# place entry field position on screen
entry.grid(row=0,column=0, columnspan=7)

# calculator buttons
button_list = ['C', 'CE', '√', '+', "pi", 'cos', 'tan', 'sin', '1', '2', '3', '-', '2pi', 'cosh', 'tanh', 'sinh',  '4', '5', '6', "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",'7', '8', '9', chr(247), "ln", "deg", "rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]

# create buttons
def button_creation(name, row, col):
    # command parameter when creating button is button functionality
    b = Button(root, width=5, height=2,bd=2,relief=SUNKEN, text=name, font=('Comic Sans MS', 16, 'bold'), activebackground='lightgray', command=lambda button=name : click(button))
    b.grid(row = row,column = col)

row = 1
col = 0

for b in button_list:
    button_creation(b, row, col)
    if col == 7:
        row += 1
        col = 0
    else:
        col += 1

# keeps window open
root.mainloop()