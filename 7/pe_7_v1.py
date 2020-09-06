# PE 7, v1
# 9-6-2020

def sieve(n):
    if(n < 2):
        return [False]
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    for i in range(2, len(primes)):
        if(primes[i]):
            for j in range(i**2, len(primes), i):
                primes[j] = False
    return primes

def nthPrime(n):
    totalPrimes = 0
    threshold = n * 2
    primes = [False]
    while (totalPrimes <= n):
        totalPrimes = 0
        primes = sieve(threshold)
        for i in range(2, threshold):
            if(primes[i]):
                totalPrimes = totalPrimes + 1
                if(totalPrimes == n):
                    return i
        threshold = threshold + n
    return -1
print(nthPrime(10001))