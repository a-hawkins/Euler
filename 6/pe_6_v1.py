# PE 6, v1
# 9-5-2020

def sumOfInts(n):
    return int((n*(n+1))/2)

def sumOfSquares(n):
    return int((n*(n+1)*(2*n+1))/6)

n = 100
print(int(sumOfInts(n)**2-sumOfSquares(n)))