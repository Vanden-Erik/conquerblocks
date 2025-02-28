import math

def primes(limit):
    primenums = [2, 3]

    for n in range(1, math.ceil((limit + 1)/6)): # Use the formula
        minus_one, plus_one = 6*n-1, 6*n+1
        primenums.append(minus_one)
        if not plus_one > limit:
            primenums.append(plus_one)
    return primenums