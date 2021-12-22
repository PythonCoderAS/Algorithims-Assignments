data = input()
numbers = [int(item) for item in data.split(" ")]

smallest = min(numbers)
numbers.remove(smallest)
second_smallest = min(numbers)
largest = max(numbers)
a = smallest
b = second_smallest
c = largest - a - b

print(a, b, c)
