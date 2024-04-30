
def get_user_dec():
    while True:
        try:
            number = int(input("Please enter the number you want to convert: "))
        except ValueError:
            print("Please only enter digits.")
        else:
            return bin(number)
        
def get_user_binary():
    while True:
        try:
            number = input("Please enter the binary you want to convert: ")
            return int(number, 2)
        except ValueError:
            print("Please only enter binary string.")

while True:
    try:
        mode = int(input("Please choose the converter mode you want (1 - binary to decimal || 2 - decimal to binary): "))
    except ValueError:
        print("Please only enter 1 or 2.")
    else:
        if mode > 2 or mode < 1:
            print("Please only enter 1 or 2")
        else:
            match(mode):
                case 1:
                    res = get_user_binary()
                case 2:
                    res = get_user_dec()
                case _:
                    pass
            
            print(f"Your conversion result is : {res}")
            break
