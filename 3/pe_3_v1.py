# PE 3, v1
# 9-4-2020

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
