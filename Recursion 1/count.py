def count(num):
	print(num)
	if (num > 0):
		count(num - 1)

count(0) # should be 0
count(4) # should be 0, 1, 2, 3, 4 (on different lines)
