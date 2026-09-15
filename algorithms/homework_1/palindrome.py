def is_palindrome(num: int) -> bool:
    n = num
    reversed_num = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        reversed_num = reversed_num * 10 + digit
    return reversed_num == num

assert(is_palindrome(121) == True)
assert(is_palindrome(123) == False)
assert(is_palindrome(1221) == True)
assert(is_palindrome(1231) == False)
assert(is_palindrome(3) == True)
assert(is_palindrome(1000) == False)
assert(is_palindrome(505) == True)
