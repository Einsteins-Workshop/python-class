locals()# See https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13, and 29.

# What is the largest prime factor of the number 600851475143?

# Replace the below with your program.

n = 600851475143
i = 2
while n != 1:
    if n % i == 0:
        n //= i
    else:
        i += 1
    print(n)
    print(i)