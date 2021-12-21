def sticker_max(lst):
    data = [0] * (len(lst) + 2)
    current_index = len(lst) - 1
    while current_index >= 0:
        data[current_index] = max(lst[current_index] + data[current_index + 2], data[current_index + 1])
        current_index -= 1
    return data[0]

print(sticker_max((6, 1, 1, 3))) # should be 9
print(sticker_max((4, 1, 2, 10, 9))) # should be 15
print(sticker_max((1, 2, 3, 4))) # should be 6
