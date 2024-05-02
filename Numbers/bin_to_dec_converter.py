from tkinter import *

# methods
def get_user_dec():

    ex = entry.get()
    print(ex)
    try:
        ex_bin = bin(int(ex))
    except:
        entry.delete(0, END)
        entry.insert(0, "Invalid digits.")
    else:
        entry.delete(0, END)
        entry.insert(0, ex_bin) 
        
def get_user_binary():
    ex = entry.get()
    print(ex)
    try:
        ex_bin = int(ex, 2)
    except:
        entry.delete(0, END)
        entry.insert(0, "Invalid input.")
    else:
        entry.delete(0, END)
        entry.insert(0, ex_bin) 

def clear():
    entry.delete(0, END)

root = Tk()

root.title("Binary|Decimal Converter")
root.config(bg="#793C5C")
root.geometry('800x200+700+100')

entry = Entry(root, font=('Comic Sans MS', 20, 'bold'), bg='white', fg='black', bd = 10, width=30)

# place entry field position on screen
entry.grid(row=1,column=0, columnspan=5)

text = Canvas(root, width=780, height=50, bd=5)
text.create_text(390, 30, text="Enter either a binary string to convert to decimals or vice versa", font=('Comic Sans MS', 15, 'bold'))
text.grid(row=0, column=0, columnspan=8)

bin_button = Button(root, width=6, height=2,bd=2,relief=SUNKEN,text="Binary", font=('Comic Sans MS', 16, 'bold'), activebackground='lightgray', command=lambda button='Binary' : get_user_dec())
bin_button.grid(row=1, column=5)

dec_button = Button(root, width=6, height=2,bd=2, relief=SUNKEN, text="Decimal", font=('Comic Sans MS', 16, 'bold'), activebackground='lightgray', command=lambda button='Binary' : get_user_binary())
dec_button.grid(row=1, column=6)

clear_button = Button(root, width=6, height=2,bd=2, relief=SUNKEN, text="Clear", font=('Comic Sans MS', 16, 'bold'), activebackground='lightgray', command=lambda button='Binary' : clear())
clear_button.grid(row=1, column=7)

root.mainloop()