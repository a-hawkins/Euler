# PE 1, v2
# 4-29-2020

target = 1000

def divisibleSum(multiple, target):
    sum = 0
    curr = multiple
    while (curr < target):
        sum = sum + curr
        curr = curr + multiple
    return sum

print(divisibleSum(3, target) + divisibleSum(5, target) - divisibleSum(15, target))
