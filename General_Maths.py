"""
Collection of general maths algorithims.
"""


def Sieve_Of_Eratosthenes(limit):
    """Returns list of primes up to limit using
       Sieve of Eratosthenes
    """
    if not isinstance(limit, int):
        raise NotIntegerError('Non integer values not accepted')

    if limit < 2:
        raise OutOfRangeError('Invalid value. Input must be greater than 1')

    primes = list(range(2, limit + 1))

    for prime in primes:
        if not prime:
            continue
        for num in range(prime*prime, limit + 1, prime):
            primes[num - 2] = None

    return [x for x in primes if x]


def find_prime_factors(num):
    """Finds the prime factors of a number
       Returns a dict object containing all prime factors
    """
    if not isinstance(num, int):
        raise NotIntegerError('Non integer values not allowed')

    if num < 2:
        raise OutOfRangeError('Invalid value. Input must be greater than 1')

    primes = Sieve_Of_Eratosthenes(num)

    factors = {}

    if num in primes:
        return {num: 1}

    while num != 1:
        for p in primes:
            while num % p == 0:
                if p in factors:
                    factors[p] += 1
                else:
                    factors[p] = 1
                num = num // p

    return factors

def Fibonacci(limit):
    """Returns Fibonacci sequence upto limit"""

    if not isinstance(limit, int):
        raise NotIntegerError('Non integer values not accepted')

    if limit < 1:
        raise OutOfRangeError('Invalid value. Input must be greater than 0')

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

    if not isinstance(num, int):
        raise NotIntegerError('Non integer values not accepted')

    if num < 1:
        raise OutOfRangeError('Invalid Value. Input must be greater than 0')

    newNum = 0

    while num != 0:
        newNum = (newNum * 10) + (num % 10)
        num = num // 10

    return newNum


def main():
    primes = [x for x in Sieve_Of_Eratosthenes(1000) if x]
    print(primes)
    print(Fibonacci(100))
    print(Reverse_Int(123))


class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass


if __name__ == "__main__":
    main()
