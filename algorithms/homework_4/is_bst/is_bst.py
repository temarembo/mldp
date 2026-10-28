class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(root):
    return _is_bst(root, None, None)


def _is_bst(root, min_value, max_value):
    if root is None:
        return True

    if min_value is not None and root.value <= min_value:
        return False

    if max_value is not None and root.value >= max_value:
        return False

    return (
        _is_bst(root.left, min_value, root.value)
        and
        _is_bst(root.right, root.value, max_value)
    )
