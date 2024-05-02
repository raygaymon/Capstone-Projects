from tkinter import *
from tkinter import ttk

unit_map = {"kg" : ['mg', 'g','tons'], "celsius" : ["fahrenheit"], "fahrenheit" : ["celcius"], "sgd" : ['yen', 'myr', 'usd']}

units = ['kg', 'celsius', 'fahrenheit', 'sgd']

prev = 0

def display_conversion(e):
    from_unit = combo.get()
    to_convert = unit_map[from_unit]
    combo_2.config(value=to_convert)
    combo_2.current(0)

def conversion():

    from_unit = combo.get()
    to_unit = combo_2.get()
    amount = entry.get()

    try:
        amount = float(amount)
    except:
        res = "Invalid digits."
    else:
    
        match(from_unit):
            case 'kg':
                res = kg_conversion(to_unit, amount)
            case 'celsius':
                res = f_conversion(amount)
            case 'fahrenheit':
                res = cel_conversion(amount)
            case 'sgd':
                res = sgd_conversion(to_unit, amount)

    result.delete('res')
    result.create_text(300, 30, text=f"Converting {amount} {from_unit} to {to_unit} is {round(res)} {to_unit}" , font=('Comic Sans MS', 15, 'bold'), tag='res')

def kg_conversion(to, amount):

    match(to):
        case 'mg':
            return amount * 1000000
        case 'g':
            return amount * 1000
        case 'ton':
            return amount/1000

def cel_conversion(amount):
    return (amount - 32) * (5/9)

def f_conversion(amount):
    return amount * (9/5) + 32

def sgd_conversion(to, amount):

    match(to):
        case 'yen':
            return amount * 114.5
        case 'usd':
            return amount * 0.74
        case 'myr':
            return amount * 3.5

# create GUI window
root = Tk()

# set GUI attributes
root.title("Unit Converter")
root.config(bg="#793C5C")
# set dimension of window - (width)x(height)+(dist from x)+(dist from y)
root.geometry('630x150+800+100')

entry = Entry(root, font=('Comic Sans MS', 10, 'bold'), bg='white', fg='black', bd = 10, width=30)

# place entry field position on screen
entry.grid(row=0,column=0, columnspan=3)

# first dropdown
combo = ttk.Combobox(root, value=units)
combo.current(0)
combo.grid(row=0, column=3, padx=5)

# bind combobox
combo.bind("<<ComboboxSelected>>", display_conversion)

# dropdown 2
combo_2 = ttk.Combobox(root, value=[""])
combo_2.current(0)
combo_2.grid(row=0, column=4, padx=5)

convert = Button(root, width=8, height=1,relief=SUNKEN, text="convert", font=('Comic Sans MS', 16, 'bold'), activebackground='lightgray', command=lambda button="convert":conversion())
convert.grid(row = 1,column = 3)

result = Canvas(root, width=600, height=60)
result.create_text(300, 15,text="")
result.grid(row=3,column=0, columnspan=8)

root.mainloop()