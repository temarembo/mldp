from functools import wraps
from time import perf_counter
import random


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start

        print(f"{func.__name__}: {elapsed:.6f} с")
        return result

    return wrapper


@measure_time
def mergesort(nums):
    def sort(arr):
        if len(arr) <= 1:
            return arr

        middle = len(arr) // 2

        left = sort(arr[:middle])
        right = sort(arr[middle:])

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    return sort(nums.copy())


@measure_time
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

    def sort(low, high):
        if low >= high:
            return

        pivot_index = partition(low, high)

        sort(low, pivot_index - 1)
        sort(pivot_index + 1, high)

    sort(0, len(arr) - 1)
    return arr


def test_sorts():
    cases = [
        [],                         # Пустой массив
        [7],                        # Один элемент
        [2, 1],                     # Два элемента
        [1, 2, 3, 4, 5],             # Уже отсортирован
        [5, 4, 3, 2, 1],             # Обратный порядок
        [4, 4, 4, 4],                # Все элементы одинаковые
        [3, -1, 0, 3, -5, 2],        # Отрицательные, ноль, повторы
        [8, 3, 7, 4, 9, 2, 6, 5],    # Смешанный порядок
    ]

    rng = random.Random(42)

    for size in range(50):
        cases.append([
            rng.randint(-20, 20)
            for _ in range(size)
        ])

    # Проверяем без декоратора, чтобы не печатать время каждого теста.
    for func in (mergesort.__wrapped__, quicksort.__wrapped__):
        for nums in cases:
            original = nums.copy()

            assert func(nums) == sorted(nums), (func.__name__, nums)
            assert nums == original

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

        assert mergesort(nums) == expected
        assert quicksort(nums) == expected


if __name__ == "__main__":
    test_sorts()
    compare()