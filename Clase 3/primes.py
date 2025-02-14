import math

limit = int(input("Limit? "))
primes = [2, 3]
not_primes = []

# An easy way to find prime numbers:
# 6n -/+ 1
# 6(1) - 1 = 5
# 6(1) + 1 = 7
# 6(2) - 1 = 11
# 6(2) + 1 = 13

print(math.floor((limit + 1) / 6))

for n in range(1, math.ceil((limit + 1)/6)): # Use the formula
    minus_one, plus_one = 6*n-1, 6*n+1
    primes.append(minus_one)
    if not plus_one > limit:
        primes.append(plus_one)

print(primes)
