def is_average(items):
    average = sum(items) / len(items)
    return average in items


n = int(input())
items = [int(number) for number in input().split(" ")]

count = 0

for start in range(n):
    for finish in range(start, n):
        if is_average(items[start:finish + 1]):
            count += 1

print(count)
