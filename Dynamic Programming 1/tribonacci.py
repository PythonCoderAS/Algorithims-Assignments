
data = {0: 0, 1:1, 2:1}
def tribonacci(n):
    if n not in data:
        value = tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
        data[n] = value
        return value
    else:
        return data[n]
