import random


def kth_largest(nums, k):
    if type(k) is not int:
        raise TypeError("k должен быть целым числом")
    if not 1 <= k <= len(nums):
        raise ValueError("k должен быть от 1 до длины массива")

    arr = nums.copy()
    target = len(arr) - k

    def partition(low, high):
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        return i

    low = 0
    high = len(arr) - 1

    while low < high:
        pivot_index = partition(low, high)

        if pivot_index == target:
            return arr[pivot_index]
        if pivot_index < target:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

    return arr[low]


def test_kth_largest():
    cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([7], 1, 7),
        ([2, 1], 1, 2),
        ([2, 1], 2, 1),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 5, 1),
        ([5, 4, 3, 2, 1], 3, 3),
        ([4, 4, 4, 4], 3, 4),
        ([-5, -1, -3, -1], 2, -1),
        ([0, -2, 0, 3], 2, 0),
        ([7, 2, 9, 4, 3, 8, 5, 1, 6], 3, 7),
    ]

    rng = random.Random(42)
    for size in range(1, 51):
        nums = [rng.randint(-20, 20) for _ in range(size)]
        expected = sorted(nums, reverse=True)
        for k in range(1, size + 1):
            cases.append((nums, k, expected[k - 1]))

    for nums in (
        list(range(1500)),
        list(range(1499, -1, -1)),
        [7] * 1500,
    ):
        expected = sorted(nums, reverse=True)
        for k in (1, 750, 1500):
            cases.append((nums, k, expected[k - 1]))

    for nums, k, expected in cases:
        original = nums.copy()
        result = kth_largest(nums, k)
        assert result == expected, (nums, k, result, expected)
        assert nums == original

    invalid_cases = [
        ([], 1, ValueError),
        ([1, 2, 3], 0, ValueError),
        ([1, 2, 3], -1, ValueError),
        ([1, 2, 3], 4, ValueError),
        ([1, 2, 3], 1.5, TypeError),
        ([1, 2, 3], "2", TypeError),
        ([1, 2, 3], True, TypeError),
    ]

    for nums, k, expected_error in invalid_cases:
        original = nums.copy()
        try:
            kth_largest(nums, k)
        except expected_error:
            pass
        else:
            raise AssertionError(f"Ожидалось исключение {expected_error.__name__}")
        assert nums == original

    print(
        f"Проверки пройдены: {len(cases)} корректных случаев "
        f"и {len(invalid_cases)} некорректных входов."
    )


if __name__ == "__main__":
    test_kth_largest()
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
