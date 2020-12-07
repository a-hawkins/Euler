# PE 6, v1
# 9-5-2020

def sumOfInts(n):
# Returns the consecutive sum of the range [1, n], 1 + 2 + 3 + ... + n
    return int((n*(n+1))/2)

def sumOfSquares(n):
# Returns the consecutive sum of squares of the range [1, n], 1^2 + 2^2 + 3^2 + ... + n^2
    return int((n*(n+1)*(2*n+1))/6)

n = 100
print(int(sumOfInts(n)**2-sumOfSquares(n)))