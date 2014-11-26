
def Sieve(max):
    numbers = list(range(2,max))
    
    for num in numbers:
        if not num:
            continue
        notPrimes = range(num+num, max, num)
        for nums in notPrimes:
            # if (nums < 1000): 
            numbers[nums - 2] = None
    return numbers

 
primes = [x for x in Sieve(1000) if x] 
print(primes) 
