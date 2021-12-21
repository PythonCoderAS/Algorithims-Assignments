def santa(n):
    data = [1, 0]
    for i in range(2, n + 1):
        if i >= len(data) - 2:
            data.append((i - 1) * (data[i - 1] + data[i - 2]))
    return data[n]

print(santa(0)) # should be 1
print(santa(1)) # should be 0
print(santa(2)) # should be 1
print(santa(3)) # should be 2
print(santa(9)) # should be 133496
