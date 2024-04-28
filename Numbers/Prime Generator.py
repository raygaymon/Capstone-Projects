import math

# got this algorithm from stackoverflow 
def prime_gen(limit):

    # instead of creating a list of numbers that need to be searched - use a list of length limit instead since accessing index is much faster + more efficient
    nums = [True] * limit

    # set 0 and 1 to False since they are not prime
    nums[0] = nums[1] = False

    for i, isprime in enumerate(nums):
        if isprime:
            yield i

            # go through the rest of the list starting from the square of i and setting every ith number to False since they are not prime
            for n in range(i * i, limit, i):
                nums[n] = False

more_please = True

while more_please:
    
    # iterating through generator to give user the choice if they want the next prime number
    for x in prime_gen(1000000):
        more_please = input("Do you want the next prime? (y/n): ").lower() == 'y'
        if more_please:
            print(f"Current prime: {x}")
        else:
            print("Okay bye")
            break



