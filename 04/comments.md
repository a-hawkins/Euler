# Largest palindrome product
### Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.   
   
Find the largest palindrome made from the product of two 3-digit numbers.   


Source: https://projecteuler.net/problem=4

## Solution 1:
```
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
```

I made a classic mistake with this problem and the next few problems. I got too caught up in the problem solving groove and wanted to rush through a few of these before the groove was lost, and I told myself I’d come back and write up my explanations after the fact, but I didn’t. This left present day me with several problems I don’t remember thinking about and several lines of code I wrote but now need to reverse engineer. The benefit to this, however, is that I have a perspective freshened with time and can find and think of things I didn’t a few months ago, and I hopefully will discover improvements along the way, as I did with this problem.   

The main functional tool this problem requires is a method of checking for palindromes. There are several valid ways to check if a string is a palindrome. Is recursion always the most safe and efficient approach for a given task? Certainly not, but it’s always satisfying when it works. Because we are only working with products of 3-digit numbers, our range of possible solutions is bounded by the following.

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\left&space;[&space;100&space;\cdot&space;100,&space;\&space;999&space;\cdot&space;999&space;\right&space;]&space;\\&space;=&space;\left&space;[&space;10000,&space;\998001&space;\right&space;]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;\left&space;[&space;100&space;\cdot&space;100,&space;\&space;999&space;\cdot&space;999&space;\right&space;]&space;\\&space;=&space;\left&space;[&space;10000,&space;\998001&space;\right&space;]" title="\large \left [ 100 \cdot 100, \ 999 \cdot 999 \right ] \\ = \left [ 10000, \998001 \right ]" /></a>

The limited range means that the palindrome checker will only be checking strings of length 5 or 6, so we don’t have to worry about overflowing the memory with a recursive function. isPalindrome(n) checks the recursively checks the first and last character of a string n. If the two characters match, the function returns a recursive call of itself on a substring of n, excluding the first and last character that were just checked. If ever the two characters being checked don’t match, a false is returned and the function ends. If the center of the string is reached (either two characters are left and they match, or only one character is left), a true is returned, as the string has been identified as a palindrome.

Where most of the optimization of this problem lies is in choosing which products to test. As established previously, the answer lies somewhere in the in the following set,   

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\left&space;\{&space;m\cdot&space;n&space;\&space;|&space;\&space;100<n,&space;m&space;<&space;999&space;\&space;\textrm{and}&space;\&space;m,&space;n&space;\in&space;\mathbb{Z}\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;\left&space;\{&space;m\cdot&space;n&space;\&space;|&space;\&space;100<n,&space;m&space;<&space;999&space;\&space;\textrm{and}&space;\&space;m,&space;n&space;\in&space;\mathbb{Z}\right&space;\}" title="\large \left \{ m\cdot n \ | \ 100<n, m < 999 \ \textrm{and} \ m, n \in \mathbb{Z}\right \}" /></a>   

which is a fancy way of saying we’re looking for a product of two integers n and m each greater than or equal to 100 and less than or equal to 999. Already, we are not checking every number between 10,000 and 998,001 because not every number in that range is a necessarily a product of two 3-digit numbers, prime numbers being the most obvious example of that. Considering that multiplication is commutative, that is m⋅n = n⋅m, the set of cases to test still includes over 405,000 possible answers to the original problem.   

In my first solution to this problem, I identified a fact to bound the potential answer set further. m⋅n is greater than m⋅(n-1), so if the current m⋅n I am testing is already less than the current largest palindrome product I have identified, I do not need to test m⋅n-1 because even if it is a palindrome, it will not be bigger than the one I already found. In my code, I swapped the order of m and n, so I decrement m until I reach a point where the product of n and m is less than my biggest palindrome, and then I finally decrement n, reset m to the new value of n, and start decrementing m again. Adding this optimization takes my work from over 405,000 cases to just 7056 cases, which is a drastic improvement.   

## Solution 2
```
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

while((n * n) > biggestPal):
    #print(n, "*", m, "=", prod)
    if(prod > biggestPal and isPalindrome(prod)):
        biggestPal = prod
    elif (prod > biggestPal):
        m = m - 1
    else:
        m = n = n-1
    prod = n * m
print(biggestPal)
```
While I looked back at my old code to try and remember why I wrote what I did, I was especially confused by my original loop condition. I couldn’t make sense of it. Not only is it redundant to be checking the value of m and n individually while also checking the product as a bound to trim out cases on the lower end, checking the values of m and n individually on their own would terminate the loop too early.   

In addition to that issue, I also decided to actually print out and look at the cases I was testing. I found a that there was a point at which I would decrement both n and reset m, but the new product was still smaller than my biggest palindrome.   

Both of these issues could be solved with a new simpler loop condition. If I reach a point where my new n times itself is less than my palindrome, no n’s and m’s less than that are going to make a bigger palindrome. This fix brought the number of cases being tested down to 6204, which isn’t as dramatic of an improvement as the previous one, but is still an improvement with the bonus of being simpler code.   
