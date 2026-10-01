def two_sum(arr, k):
    seen = {}
    for i, num in enumerate(arr):
        target = k - num
        if target in seen:
            return seen[target], i
        else:
            seen[num] = i

assert two_sum([1, 3, 4, 10], 7) == (1, 2)
assert two_sum([5, 5, 1, 4], 10) == (0, 1)
assert two_sum([2, 7, 11, 15], 9) == (0, 1)
assert two_sum([3, 2, 4], 6) == (1, 2)
assert two_sum([-3, 4, 3, 90], 0) == (0, 2)
assert two_sum([0, 4, 3, 0], 0) == (0, 3)
assert two_sum([1, 2], 3) == (0, 1)
