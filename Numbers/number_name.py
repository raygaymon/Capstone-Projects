digit_to_name = {1 : 'one', 2 : 'two', 3 : "three", 4 : "four", 5 :'five', 6 :"six", 7 : "seven", 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : "twelve", 13 : "thirteen", 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}

tens = {2 : 'twenty', 3 : 'thirty', 4 : 'fourty', 5 :'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}

def convert(num):

    if num == 0:
        return
    
    res = ''

    # check for millions
    million = int(num/1000000)
    if million > 0:
        # run recursively to get the 100s portion of the million
        res += convert(million)
        res += " million "

    num = num%1000000

    # check for thousands
    thousand = int(num/1000)

    if thousand > 0:

        # run recursively to get the 100s portion of the thousands
        res += convert(thousand)
        res += " thousand "
    
    num = num % 1000

    # runs the 100s portion
    hundred = int(num/100)
    if hundred > 0:
        res += digit_to_name[hundred]
        res += " hundred "
    
    num = num%100

    # due to special names of < 20s skip the tens check
    if num < 20 :
        res += digit_to_name[num]
    else:
        # get 10s name
        ten = int(num/10)
        if ten > 0:
            res += tens[ten] + " "
        # get single digit name
        num = num%10
        if num > 0:
            res += digit_to_name[num]
    
    return res

def main():
    while True:
        to_convert = input("Enter the number to convert into name: ")
        try:
            to_convert = int(to_convert)
        except ValueError:
            print("Not a valid number.")
        else:
            print(convert(to_convert))
            break

if __name__ == "__main__":
    main()