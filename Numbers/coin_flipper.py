from random import randint

def coin_flip():
    side = randint(1,2)

    if side == 1 :
        return 'heads'
    else:
        return 'tails'

def main():

    results = {'heads' : 0, 'tails' : 0}
    try:
        flips = int(input("How many times do you want to flip the coin: "))
    except ValueError:
        print("Please enter a valiud digit.")
    else:
        for i in range(flips):
            r = coin_flip()
            results[r] += 1

    print(f"Results of {flips} flips:\nHeads: {results['heads']} | Tails: {results['tails']}")

if __name__ == '__main__':
    main()
        
    
