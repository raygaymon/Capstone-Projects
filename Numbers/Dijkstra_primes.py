from heapq import heapify, heappush, heappop

# my personal attempt at implementing Dijkstra's Prime number generating algorithm as explained by boo1
# youtube video here: https://www.youtube.com/watch?v=fwxjMKBMR7s

def dijkstra(n):

    # since dijkstra's method requires checking of the smallest composite value, I decided to use a min heap to accomplish that automatically
    # decided to use tuples since I can also acquire the base prime of the composite as well
    prime_squares_heap = [(4, 2)]
    heapify(prime_squares_heap)

    # FINAL LIST OF PRIMES
    primes = [2]

    for i in range(3, n):

        # extract the minimum composite value as well as its associated prime
        min_val, prime = prime_squares_heap[0]

        # if the current value being checked is smaller than the smallest composite value then it is a prime
        if i < min_val:
            print(f"{i} is a prime. ")

            # yield the prime as this script is intended to provide primes so long as users continue to want primes
            yield i

            # add the prime to the list of prime
            primes.append(i)
            
            # adding the prime and its square to the primes min heap
            heappush(prime_squares_heap, (i**2, i))

        else:

            # i is larger or equal to the smallest composite -> it is not a prime and we have to update the smallest composite value(s)
            # min_val is the current smallest composite - passing it in for comparison
            update_primes(prime_squares_heap, min_val)


def update_primes(heap, min_val):

    # made it a while loop as there might be multiple instances of the current smallest composite
    # e.g. 2 and 3 will both have 12 as their composite when checking 12 -> both must be updated (14, 15) so that 13 will be less than the new smallest
    while True:

        # extracting the current smallest composite tuple
        k, v = heap[0]

        # the current smallest composite is == to min_val
        if k == min_val:

            # popping the min_val composite tuple out of the heap
            heappop(heap)

            # creating a new tuple with updated values
            new_val = (k + v, v)

            # adding the newly updated tuple back into the heap
            heappush(heap, new_val)
        else:
            # the current smallest value in the tuple is larger than the min_val we were comparing - break out of updating
            break

more_primes = True

while more_primes:
    
    # iterating through generator to give user the choice if they want the next prime number
    for x in dijkstra(1000000):

        # any input that is not Y will terminate the script
        more_please = input("Do you want the next prime? (y/n): ").lower() == 'y'
        if more_please:
            print(f"Current prime (Sponsored by Daddy Dijkstra): {x}")
        else:
            print("Okay bye")
            more_primes = False
            break