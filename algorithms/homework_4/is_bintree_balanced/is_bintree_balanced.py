class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    return _height(root) != -1


def _height(root):
    if root is None:
        return 0

    left_height = _height(root.left)

    if left_height == -1:
        return -1

    right_height = _height(root.right)

    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1
