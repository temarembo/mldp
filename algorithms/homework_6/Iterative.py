import random
from time import perf_counter


def mergesort(nums):
    arr = nums.copy()
    n = len(arr)
    buffer = arr.copy()
    width = 1

    while width < n:
        for start in range(0, n, 2 * width):
            middle = min(start + width, n)
            end = min(start + 2 * width, n)

            i = start
            j = middle
            k = start

            while i < middle and j < end:
                if arr[i] <= arr[j]:
                    buffer[k] = arr[i]
                    i += 1
                else:
                    buffer[k] = arr[j]
                    j += 1
                k += 1

            while i < middle:
                buffer[k] = arr[i]
                i += 1
                k += 1

            while j < end:
                buffer[k] = arr[j]
                j += 1
                k += 1

        arr, buffer = buffer, arr
        width *= 2

    return arr


def quicksort(nums):
    arr = nums.copy()

    def partition(low, high):
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        return i

    stack = []
    if len(arr) > 1:
        stack.append((0, len(arr) - 1))

    while stack:
        low, high = stack.pop()
        pivot_index = partition(low, high)

        # Стек LIFO: правый участок кладём первым, чтобы левый обработать раньше.
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

        if low < pivot_index - 1:
            stack.append((low, pivot_index - 1))

    return arr


def test_sorts():
    cases = [
        [],
        [7],
        [2, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 4, 4, 4],
        [3, -1, 0, 3, -5, 2],
        [8, 3, 7, 4, 9, 2, 6, 5],
        [9, 3, 7, 1, 8, 2, 6],
        [9, 3, 7, 1, 8, 2, 6, 4, 5],
        [2, 1, 2, 1, 2],
    ]

    rng = random.Random(42)
    for size in range(100):
        cases.append([rng.randint(-50, 50) for _ in range(size)])

    # Эти входы требуют линейной глубины вызовов в рекурсивном quicksort.
    cases.extend([
        list(range(1500)),
        list(range(1499, -1, -1)),
        [7] * 1500,
    ])

    for func in (mergesort, quicksort):
        for nums in cases:
            original = nums.copy()
            result = func(nums)

            assert result == sorted(nums), (func.__name__, nums)
            assert nums == original
            assert result is not nums

    print(
        f"Проверки пройдены: {len(cases)} массивов "
        "для каждого алгоритма."
    )


def compare():
    n = 600
    rng = random.Random(42)
    cases = {
        "Случайный массив": rng.sample(range(n * 10), n),
        "По возрастанию": list(range(n)),
        "По убыванию": list(range(n - 1, -1, -1)),
        "Одинаковые элементы": [7] * n,
    }

    for name, nums in cases.items():
        print(f"\n{name}, n = {n}")
        expected = sorted(nums)
        original = nums.copy()

        for func in (mergesort, quicksort):
            start = perf_counter()
            result = func(nums)
            elapsed = perf_counter() - start

            assert result == expected, (name, func.__name__)
            assert nums == original
            print(f"{func.__name__}: {elapsed:.6f} с")


if __name__ == "__main__":
    test_sorts()

    nums = [9, 3, 7, 1, 8, 2, 6]
    print("Исходный массив:", nums)
    print("Mergesort:", mergesort(nums))
    print("Quicksort:", quicksort(nums))
    compare()
