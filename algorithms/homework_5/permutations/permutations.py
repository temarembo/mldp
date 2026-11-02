from functools import wraps


def tracer(func):
    depth = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth

        indent = "    " * depth

        arguments = [repr(arg) for arg in args]
        arguments += [
            f"{key}={value!r}"
            for key, value in kwargs.items()
        ]

        arguments_str = ", ".join(arguments)

        print(
            f"{indent}-> {func.__name__}({arguments_str})"
        )

        depth += 1

        try:
            result = func(*args, **kwargs)
        finally:
            depth -= 1

        print(
            f"{indent}<- {func.__name__}({arguments_str}) = {result!r}"
        )

        return result

    return wrapper

@tracer
def permutations(nums): # считаю что в массиве нет повторений
    if len(nums) == 1:
        return [nums]

    result = []
    for i in range(len(nums)):
        nums_copy = nums.copy()
        num = nums_copy.pop(i)
        for permutation in permutations(nums_copy):
            result.append([num] + permutation)
    return result

print(permutations([1,2,3]))
