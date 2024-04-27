from mpmath import mp

def get_pi():

    digits = 0

    # to protect against invalid inputs
    while True:
        try:
            digits = int(input("How many digits of PI do you want ( 1 - 99 ): "))
        except:
            print("Please give a digit.")
        else:
            # set upper limits and prevent negative decimals
            if digits > 99 or digits < 0:
                print("Please only go between 1 and 99")
            else:
                break

    mp.dps = digits
    print(f"{digits} decimals of PI is {mp.pi}")

def get_e():
    digits = 0

    while True:
        try:
            digits = int(input("How many digits of e do you want ( 1 - 99 ): "))
        except:
            print("Please give a digit.")
        else:
            if digits > 99 or digits < 0:
                print("Please only go between 1 and 99")
            else:
                break

    mp.dps = digits
    print(f"{digits} decimals of e is {mp.e}")


