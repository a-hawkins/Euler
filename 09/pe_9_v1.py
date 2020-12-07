# PE 8 v1
# 9-6-2020

def generateTriple(m, n):
# Generates a pythagorean triple fot m > n > 0
    return [(m**2 - n**2), (2*n*m), (m**2 + n**2)]


def isCoprime(a, b):
# Returns True if a and b are coprime, and False otherwise.
# Two values are considered coprime if they share no common prime factors
    return (gcd(a,b) == 1)

def gcd(a, b):
# Returns the greatest common factor of a and b using Euclid's algorithm
    if a < b:
        temp = a
        a = b
        b = temp

    r = a % b

    while(r > 0):
        a = b
        b = r
        r = a % b
    return b

def specialTriple(n):
# Returns a pythagorean tripple [a, b, c] such that a + b + c = n
    i = 0
    primativeTriple = triple = [0, 0, 0]
    while (sum(triple) != n):
        j = 1
        i  = i + 1
        primativeTriple = triple = generateTriple(i, j)
        while(j < i and sum(triple) < n):
            if ((i % 2 == 0 or j % 1 == 0) and not isCoprime(i, j)):
                k = 1
                while(sum(triple) < n):
                    k = k + 1
                    triple = [x*k for x in primativeTriple]
            j = j + 1
    return triple

triple = specialTriple(1000)
print(triple[0]*triple[1]*triple[2])
    



    