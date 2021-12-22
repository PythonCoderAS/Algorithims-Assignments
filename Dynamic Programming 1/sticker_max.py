def sticker_max(lst):
    if lst not in data:
        value = max(lst[0] + sticker_max(lst[2:]), sticker_max(lst[1:]))
        data[lst] = value
        return value
    else:
        return data[lst]

print(sticker_max((6, 1, 1, 3))) # should be 9
print(sticker_max((4, 1, 2, 10, 9))) # should be 15
print(sticker_max((1, 2, 3, 4))) # should be 6
