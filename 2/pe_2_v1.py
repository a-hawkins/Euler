# PE 2, v1
# 5-14-2020

sum = 0
prev = 0
curr = 1

while (curr <= 4000000):
    if(curr % 2 == 0):
        sum = sum + curr
    temp = curr
    curr = curr + prev
    prev = temp
    
print(sum)

