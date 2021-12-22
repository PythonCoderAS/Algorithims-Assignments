def factorial(num):
	if num <= 1:
		return num
	else:
		return num * factorial(num - 1)


print(factorial(4)) # should be 24
print(factorial(1)) # should be 1
print(factorial(0)) # should be 0
