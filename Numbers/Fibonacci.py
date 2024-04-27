import time

def fibonacci(n, memo):

    if n < 0:
        memo[0] = 0
        return 0
    elif n == 1:
        memo[n] = 1
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            res = fibonacci(n-1, memo) + fibonacci(n-2, memo)
            memo[n] = res
            return res

def execute():

    memo = {}
    n = 0

    while True:
        try:
            n = int(input("How much of the Fibonacci sequence do you want to generate (1 - 40): "))
        except ValueError:
            print("Please input a number.")
        else:
            if n < 0:
                print("Please enter a positive number.")
            elif n > 40:
                print("More than 40 take too long go away.")
            else:
                break

    res = fibonacci(n, memo)
    vals = list(memo.values())
    vals.sort()
    print(f"The {n}th fibonacci number is {res}.")
    print("The sequence is as follows: ")
    print(*vals)

    

if __name__ == '__main__':
    start_time = time.time()
    execute()
    end_time = time.time()
    print(f"Fibonacci sequence took {round(end_time - start_time, 4)} seconds to run.")