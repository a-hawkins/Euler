# Largest Prime Factor
### Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Source: https://projecteuler.net/problem=3   
   
## Solution 1:
```
def largestPrime(n):
    largest = 1
    i = 2
    if(n%i==0):
        largest = i
        while(n%i==0):
            n = n/i
    i = 3
    while(i <= n):
        if(n%i==0):
            largest = i
            while(n%i==0):
                n = n/i
        i = i + 2
    return largest

print(largestPrime(600851475143))
```
My initial idea for this problem was to find all of the primes less than or equal to half of the target number, then iterate through them from greatest to least until I found the first prime p that divided evenly into the target number n (such that n mod p == 0). The thinking here was that I could be a little more efficient by starting with the big numbers and not having to check every prime less than the largest prime factor before I found that prime. I eventually came to realize that idea had a bit of an oversight in that generating the primes would already require doing work to identify those smaller primes, so I wouldn't be saving work at all. I would be doing more.

My revised strategy is destructive to n. By starting from the lower end of the primes and dividing out each instance of a prime factor from n before moving on to the next i, I ensure that I won't falsely claim that a composite number is the largest prime. By the time i reaches a composite number, n should no longer be divisible by that composite number because I've already divided out all of that compsite number's prime factors.