# Multiples of 3 and 5
### Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.   

Source: https://projecteuler.net/problem=1   

## Solution 1:
A more intuitive yet less effecient approach. It simply runs through each of the natural numbers below 1000, 
checks if it is a multiple of 3 or 5, and if so, adds it to a running total.   

I chose python because it handles large numbers without hassle and would let me get my ideas out quickly.   

## Solution 2:
Solution 1 runs quickly enough for the size of the data set that needs processing in this problem, 
but it does a lot of work it doesn't have to. Rather than checking each number to see if it is a multiple of 3 or 5, 
we can just skip ahead directly to each multiple, find subtotals for the sums of the multiples of 3 less than 1000 and multiples of 5 
less than 1000 seperately, and add those together. Some numbers, however, are multiples of both 3 and 5, so they would be double 
counted in this method, causing the final total to be too high. To counteract this issue, we must also find the sum of all multiples 
of 15 less than 1000 and subtract that sum from our total sum, elimintating all overlap.

Rather than retype almost the same code three-times over, it's better at this point to make a reusable function 

## Solution 3:
Here we take the ideas of Solution 2 and refine it further using a well-known summation formula to elimiate the need for looping.
The sum of the multiples of a number m less than a target t can be found by calculating the consecutive sum of the interval [1, floor(t/m)] 
and multiplying that sum by m.   

To understand this better, let's look at adding up multiples of 3 less than 1000.   
Our largest number in this series will be 999, which is 1000 divided by 3 rounded down.   

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;3&space;&plus;&space;6&space;&plus;&space;9&space;&plus;&space;12&space;&plus;&space;...&space;&plus;&space;999" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;3&space;&plus;&space;6&space;&plus;&space;9&space;&plus;&space;12&space;&plus;&space;...&space;&plus;&space;999" title="\large 3 + 6 + 9 + 12 + ... + 999" /></a>   

Because all of these numbers are multiples of 3, we can pull out the three to the front of each number.   

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;=&space;3(1)&space;&plus;&space;3(2)&space;&plus;&space;3(3)&space;&plus;&space;...&space;&plus;&space;3*333" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;=&space;3(1)&space;&plus;&space;3(2)&space;&plus;&space;3(3)&space;&plus;&space;...&space;&plus;&space;3*333" title="\large = 3(1) + 3(2) + 3(3) + ... + 3*333" /></a>   

Using the distributive property, we can pull out the three even further.   

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;=&space;3(1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;...&space;&plus;&space;333)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;=&space;3(1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;...&space;&plus;&space;333)" title="\large = 3(1 + 2 + 3 + ... + 333)" /></a>   

A consecutive sum 
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;...&space;&plus;&space;n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\large&space;1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;...&space;&plus;&space;n" title="\large 1 + 2 + 3 + ... + n" /></a> 
can be found by using the consecutive sum formula:   
 
 <a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\sum_{i=1}^{n}i=\frac{n(n&plus;1)}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;\sum_{i=1}^{n}i=\frac{n(n&plus;1)}{2}" title="\large \sum_{i=1}^{n}i=\frac{n(n+1)}{2}" /></a>   

Therefore, we find the following to be true:   

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;3\left&space;(1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;...&space;&plus;&space;333\right)=&space;3*\sum_{i=1}^{333}i=3&space;\left&space;[&space;\frac{333(333&plus;1)}{2}&space;\right&space;]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;3\left&space;(1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;...&space;&plus;&space;333\right)=&space;3*\sum_{i=1}^{333}i=3&space;\left&space;[&space;\frac{333(333&plus;1)}{2}&space;\right&space;]" title="\large 3\left (1 + 2 + 3 + ... + 333\right)= 3*\sum_{i=1}^{333}i=3 \left [ \frac{333(333+1)}{2} \right ]" /></a>   

Generalizing it for any number m and target t so we can make a nice and friendly reusable function, we get the following equation:   

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;m\left&space;(1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;...&space;&plus;&space;\left&space;\lfloor&space;\frac{t}{m}&space;\right&space;\rfloor&space;\right)&space;=&space;m*\sum_{i=1}^{\left&space;\lfloor&space;\frac{t}{m}&space;\right&space;\rfloor}i&space;=&space;m&space;\left&space;[&space;\frac{\left&space;\lfloor&space;\frac{t}{m}&space;\right&space;\rfloor(\left&space;\lfloor&space;\frac{t}{m}&space;\right&space;\rfloor&plus;1)}{2}&space;\right&space;]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;m\left&space;(1&space;&plus;&space;2&space;&plus;&space;3&space;&plus;&space;...&space;&plus;&space;\left&space;\lfloor&space;\frac{t}{m}&space;\right&space;\rfloor&space;\right)&space;=&space;m*\sum_{i=1}^{\left&space;\lfloor&space;\frac{t}{m}&space;\right&space;\rfloor}i&space;=&space;m&space;\left&space;[&space;\frac{\left&space;\lfloor&space;\frac{t}{m}&space;\right&space;\rfloor(\left&space;\lfloor&space;\frac{t}{m}&space;\right&space;\rfloor&plus;1)}{2}&space;\right&space;]" title="\large m\left (1 + 2 + 3 + ... + \left \lfloor \frac{t}{m} \right \rfloor \right) = m*\sum_{i=1}^{\left \lfloor \frac{t}{m} \right \rfloor}i = m \left [ \frac{\left \lfloor \frac{t}{m} \right \rfloor(\left \lfloor \frac{t}{m} \right \rfloor+1)}{2} \right ]" /></a>   

In my python implementation of this equation, integer truncation takes care of the floor function (aka always rounding down). 
To squeeze out an extra little bit of efficiency, floor(m/t) is only calculated once and then stored since it is used multiple times. 
Additional integer typcasting on the retrun of the function's calculation is my lazy way of reformatting the output without a decimal
because python adds one one one by default when dividing.   

The final product has the same basic structure as solution 2 with a revamped divisibleSum function. 
The nature of this implementation requires us to set the target to 999 rather than 1000 to meet the strictly "less than" 
requirments of the instructions previously handled by loop conditions in earlier solutions.

