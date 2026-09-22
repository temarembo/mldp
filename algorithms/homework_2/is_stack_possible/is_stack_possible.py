def is_stack_possible(pushed, popped):
    pushed_list = [int(num) for num in pushed.split()]
    popped_list = [int(num) for num in popped.split()]

    stack = []
    j = 0

    for i in pushed_list:
        stack.append(i)

        while (stack and j < len(popped_list) and stack[-1] == popped_list[j]):
            stack.pop()
            j += 1

    return j == len(popped_list)

assert is_stack_possible(
    "1 2 3 4 5",
    "1 3 5 4 2"
) is True

# Полностью прямой порядок: push -> сразу pop
assert is_stack_possible(
    "1 2 3 4 5",
    "1 2 3 4 5"
) is True

# Полностью обратный порядок: сначала всё кладём в стек
assert is_stack_possible(
    "1 2 3 4 5",
    "5 4 3 2 1"
) is True

# Невозможный порядок
assert is_stack_possible(
    "1 2 3 4 5",
    "4 3 5 1 2"
) is False

# Ещё один невозможный порядок
assert is_stack_possible(
    "1 2 3",
    "3 1 2"
) is False

# Один элемент
assert is_stack_possible(
    "1",
    "1"
) is True

# Два элемента в прямом порядке
assert is_stack_possible(
    "10 20",
    "10 20"
) is True

# Два элемента в обратном порядке
assert is_stack_possible(
    "10 20",
    "20 10"
) is True
