from collections import defaultdict
prime_factors = defaultdict(lambda: 0)

def find_primes(n):
    original = n
    i = 2

    while i * i < n:
        while n % i == 0:
            prime_factors[i] = prime_factors[i] + 1
            n = n / i
        i += 1

    if n > 0 and n != original:
        prime_factors[int(n)] = 1
    

while True:
    try:
        n = int(input("Enter the number whose prime factors you want to find: "))
    except ValueError:
        print("Please put in a number.")
    else:
        if n < 0:
            print("Please enter a positve number.")
        else:
            original = n
            find_primes(n)
            answer = ""
            for i, k in enumerate(prime_factors.keys()):
                answer += f"{k} ^ {prime_factors[k]}"
                if i < len(prime_factors.keys()) - 1:
                    answer += " + "

            print(f"The prime factors of {original} are: \n{answer}")
            
            print("Your're welcome")
            break