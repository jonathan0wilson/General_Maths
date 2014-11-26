
def Sieve(limit):
    primes = list(range(2,limit))
    
    for prime in primes:
        if not prime:
            continue
        for num in range(prime*prime, limit, prime):
            primes[num - 2] = None
    return primes

def main(): 
    primes = [x for x in Sieve(1000) if x] 
    print(primes)

if __name__ == "__main__":
    main()
