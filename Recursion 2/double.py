def double(st1):
    if len(st1) > 1:
        return double(st1[0]) + double(st1[1:])
    else:
        return st1 * 2


print(double('cake')) # should be 'ccaakkee'
print(double('banana')) # should be 'bbaannaannaa'
print(double('g')) # should be 'gg'
