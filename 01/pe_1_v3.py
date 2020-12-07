# PE 1, v3
# 4-29-2020

target = 999

def divisibleSum(multiple, target):
	n = int(target/multiple)
	return int(multiple * (n*(n+1))/2)

print(divisibleSum(3, target) + divisibleSum(5, target) - divisibleSum(15, target))
