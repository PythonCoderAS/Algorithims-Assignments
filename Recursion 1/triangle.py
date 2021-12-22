def triangle(num):
	print("O" * num)
	if num > 1:
		triangle(num - 1)


triangle(3)
# should make
# OOO
# OO
# O
