# PE 1, v1
# 4-14-2020

sum = 0
for i in range (1000):
    if(i % 3 == 0 or i % 5 == 0):
        sum = sum + i
print(sum)
