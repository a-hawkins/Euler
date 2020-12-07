# PE 5, v1
# 9-5-2020

def smallestMultiple(n):
# Returns the smallest multiple of all natural numbers <=n
    factorList = [0]*(n+1)
    for k in range(2,n+1):
        i = 2
        primeCount=0
        while(k%i==0):
            k = k/i
            primeCount = primeCount + 1
        if (factorList[i] < primeCount):
                factorList[i] = primeCount
                
        primeCount = 0
        i = 3
        while(k > 1):
            while(k%i==0):
                k = k/i
                primeCount = primeCount + 1
            
            if (factorList[i] < primeCount):
                factorList[i] = primeCount

            primeCount = 0
            i = i + 2
            
    prod = 1
    print(factorList)
    for i in range(2, n+1):
        if (factorList[i]>0):
            prod = prod*((i)**factorList[i])
    return prod
print(smallestMultiple(20))