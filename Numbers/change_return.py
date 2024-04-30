total = 0
paid = 0

while True:
    try:
        total = float(input(f"How much do you need to pay: "))
    except ValueError:
        print("Please only enter digits.")
    else:
        break

while True:
    try:
        paid = float(input(f"How much did you to pay: "))
    except ValueError:
        print("Please only enter digits.")
    else:
        break

change = paid - total
if change < 0:
    print("You did not pay enough.")
else:
    change *= 100

    quarters = change / 25

    change = change % 25

    dimes = change / 10

    change = change % 10

    nickels = change / 5

    change = change % 5

    print(f"After paying {round(paid)}, you will get back {round(quarters)} quarters, {round(dimes)} dimes, {round(nickels)} nickels, and {round(change)} pennies. ")