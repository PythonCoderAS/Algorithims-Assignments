def is_palindrome(st1):
    if len(st1) <= 1:
        return True
    else:
        return st1[0] == st1[-1] and is_palindrome(st1[1:-1])

print(is_palindrome('noon')) # should be True
print(is_palindrome('starts')) # should be False
print(is_palindrome('onion')) # should be False
print(is_palindrome('v')) # should be True
