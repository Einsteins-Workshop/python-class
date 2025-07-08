def prime(n: int) -> bool:
    if n < 0:
        return prime(n*-1)
    if n in [0, 1]:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(1, 10001):
    if prime(i):
        print("-", end="")
    else:
        print(".", end="")
    if i % 200 == 0:
        print()