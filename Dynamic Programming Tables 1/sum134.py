def sum134(n):
    data = [1, 1, 1, 2]
    for i in range(4, n + 1):
        if i >= len(data) - 4:
            data.append(data[i - 1] + data[i - 3] + data[i - 4])
    return data[n]

print(sum134(0)) # should be 1
print(sum134(1)) # should be 1
print(sum134(2)) # should be 1
print(sum134(3)) # should be 2
print(sum134(4)) # should be 4
print(sum134(8)) # should be 25
