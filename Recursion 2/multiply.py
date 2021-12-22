def multiply(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    elif num2 == 1:
        return num1
    elif num1 == 1:
        return num2
    else:
        return num1 + multiply(num1, num2 - 1)


print(multiply(3, 5)) # should be 15
print(multiply(0, 4)) # should be 0
print(multiply(2, 1)) # should be 2
