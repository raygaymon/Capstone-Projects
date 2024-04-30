
mortgage_amount = "mortgage amount"
duration_of_payment = "payment term (years)"
interest_rate = "interest rate"

def user_input(parameter):

    while True:
        try:
            parameter = int(input(f"Enter your {parameter}: "))
        except ValueError:
            print("Please only enter digits.")
        else:
            return parameter

mortgage_amount = user_input(mortgage_amount)
duration_of_payment = user_input(duration_of_payment)
interest_rate = user_input(interest_rate)/1200
months_of_payment = duration_of_payment * 12


monthly_payment = mortgage_amount * ((interest_rate)*((interest_rate + 1) ** months_of_payment))/((interest_rate + 1) ** (months_of_payment)-1)

while True:
    desired_period = input("Please indicate what kind of compounding method you would like to see (minute, hourly, daily, weekly, monthly, yearly): ")
    match(desired_period):
        case 'monthly':
            print(f"Your monthly payment for this mortage of {mortgage_amount} over {duration_of_payment} years is ${round(monthly_payment, 2)} per month.")
            break
        case 'weekly':
            weekly_payment = monthly_payment/4
            print(f"Your weekly payment for this mortage of {mortgage_amount} over {duration_of_payment} years is ${round(weekly_payment, 2)} per week.")
            break
        case 'daily':
            daily_payment = monthly_payment/28
            print(f"Your daily payment for this mortage of {mortgage_amount} over {duration_of_payment} years is ${round(daily_payment, 2)} per day.")
            break
        case 'hourly':
            hourly_payment = monthly_payment/672
            print(f"Your hourly payment for this mortage of {mortgage_amount} over {duration_of_payment} years is ${round(hourly_payment, 2)} per hour.")
            break
        case 'minute':
            minute_payment = monthly_payment/40320
            print(f"Your minute payment for this mortage of {mortgage_amount} over {duration_of_payment} years is ${round(minute_payment, 2)} per minute.")
            break
        case 'yearly':
            yearly_payment = monthly_payment * 12
            print(f"Your yearly payment for this mortage of {mortgage_amount} over {duration_of_payment} years is ${round(yearly_payment, 2)}.")
            break
        case _:
            print("Please enter a valid input.")