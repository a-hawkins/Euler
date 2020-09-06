# PE 10, v1
# 9-6-2020

def sieve(n):
# Retuens a boolean array of size n+1 representing which numbers less than
#   or equal to n are prime
    if(n < 2):
        return [False]
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    for i in range(2, len(primes)):
        if(primes[i]):
            for j in range(i**2, len(primes), i):
                primes[j] = False
    return primes

def primeSummation(n):
# Return the sum of all primes less than or equal to n
    primes = sieve(n)
    total = 0
    for i in range(len(primes)):
        if (primes[i]):
            total+= i
    return(total)

print(primeSummation(2000000))