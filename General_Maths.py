"""
Collection of general maths algorithims.
"""


def Sieve_Of_Eratosthenes(limit):
    """Returns list of primes up to limit using
       Sieve of Eratosthenes
    """
    primes = list(range(2, limit))

    for prime in primes:
        if not prime:
            continue
        for num in range(prime*prime, limit, prime):
            primes[num - 2] = None
    return [x for x in primes if x]


def Fibonacci(limit):
    """Returns Fibonacci sequence upto limit"""
    fibonacci = [1, 1]

    AtLimit = False

    while(not AtLimit):
        if fibonacci[-1] + fibonacci[-2] < limit:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        else:
            AtLimit = True

    return fibonacci


def Reverse_Int(num):
    """Returns the number reversed"""
    newNum = 0

    while num != 0:
        newNum = (newNum * 10) + (num % 10)
        num = num // 10

    return num


def main():
    primes = [x for x in Sieve_Of_Eratosthenes(1000) if x]
    print(primes)
    print(Fibonacci(100))

if __name__ == "__main__":
    main()
