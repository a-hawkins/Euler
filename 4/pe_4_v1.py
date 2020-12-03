# PE 4, v1
# 9-4-2020

def isPalindrome(n):
# Recursively checks if a string n is a palindrome and returns a boolean
    n = str(n)
    if(len(n) == 1 or (len(n)==2 and n[0]==n[1])):
        return True
    if (n[0] != n[-1]):
        return False
    return isPalindrome(n[1: -1])

n = m = 999
biggestPal = 1
prod = n*m

while(n > 0 and m > 0 and prod > 10000):
    #print(n, "*", m, "=", prod)
    if(prod > biggestPal and isPalindrome(prod)):
        biggestPal = prod
    elif (prod > biggestPal):
        m = m - 1
    else:
        m = n = n-1
    prod = n * m
print(biggestPal)

