def max_even_sum(nums: str) -> int:
    nums_list = [int(num) for num in nums.split()]
    sum_all = sum(nums_list)
    min_odd = float('inf')
    for num in nums_list:
        if num % 2 == 1:
            min_odd = min(min_odd, num)
    if sum_all % 2 == 0:
        return sum_all
    else:
        return sum_all - min_odd

assert max_even_sum("1 2 3 4") == 10
assert max_even_sum("1 2 3 4 5") == 14
assert max_even_sum("1 3 4 5 6") == 18
assert max_even_sum("1") == 0
assert max_even_sum("2") == 2
assert max_even_sum("2 4 6") == 12
assert max_even_sum("1 3 5") == 8
assert max_even_sum("3 5") == 8
assert max_even_sum("7 2 8 3") == 20
