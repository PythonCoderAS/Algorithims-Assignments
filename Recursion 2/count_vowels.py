def count_vowels(st1):
    if len(st1) == 0:
        return 0
    else:
        return (1 if st1[0] in "aeiou" else 0) + count_vowels(st1[1:])

print(count_vowels('rhythm')) # should be 0
print(count_vowels('area')) # should be 3
print(count_vowels('gnomon')) # should be 2
