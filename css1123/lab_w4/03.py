

def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True


def next_prime(N):
    N += 1
    while not is_prime(N):
        N += 1
    return N


def next_twin_prime(N):
    number1 = next_prime(N)
    number2 = next_prime(number1)
    while number2 - number1 != 2:
        number1 = number2
        number2 = next_prime(number1)
    return number1, number2


exec(input().strip())