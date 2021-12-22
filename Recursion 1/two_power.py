def two_power(num):
	if num == 0:
		return 0
	elif num == 1:
		return 2
	else:
		return 2 * two_power(num - 1)



print(two_power(4)) # should be 16
print(two_power(1)) # should be 2
print(two_power(0)) # should be 0
