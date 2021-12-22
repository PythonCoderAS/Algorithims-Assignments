data = {0: 1, 1: 0, 2: 1}
def santa(n):
    if n in data:
        return data[n]
    else:
        val = (n-1) * (santa(n - 1) + santa(n - 2))
        data[n] = val
        return val

print(santa(0)) # should be 1
print(santa(1)) # should be 0
print(santa(2)) # should be 1
print(santa(3)) # should be 2
print(santa(9)) # should be 133496
