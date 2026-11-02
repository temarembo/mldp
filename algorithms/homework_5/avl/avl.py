class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(
            self._height(node.left),
            self._height(node.right)
        )

    def _balance_factor(self, node):
        if node is None:
            return 0

        return (
            self._height(node.left)
            - self._height(node.right)
        )

    def _rotate_right(self, y):
        x = y.left
        subtree = x.right

        x.right = y
        y.left = subtree

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        subtree = y.left

        y.left = x
        x.right = subtree

        self._update_height(x)
        self._update_height(y)

        return y

    def _rebalance(self, node):
        self._update_height(node)

        balance = self._balance_factor(node)

        # Left-heavy
        if balance > 1:
            # Left-Right
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)

            # Left-Left
            return self._rotate_right(node)

        # Right-heavy
        if balance < -1:
            # Right-Left
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)

            # Right-Right
            return self._rotate_left(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)

        elif value > node.value:
            node.right = self._insert(node.right, value)

        else:
            # Дубликаты не добавляем
            return node

        return self._rebalance(node)

    def search(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            # Нет левого ребёнка
            if node.left is None:
                return node.right

            # Нет правого ребёнка
            if node.right is None:
                return node.left

            # Есть два ребёнка:
            # берём минимальный узел из правого поддерева
            successor = self._find_min(node.right)

            node.value = successor.value

            node.right = self._delete(
                node.right,
                successor.value
            )

        return self._rebalance(node)

    def _find_min(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return

        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)


# -------------------------
# TESTS
# -------------------------

# LL rotation
tree = AVL()

tree.insert(30)
tree.insert(20)
tree.insert(10)

assert tree.root.value == 20
assert tree.inorder() == [10, 20, 30]


# RR rotation
tree = AVL()

tree.insert(10)
tree.insert(20)
tree.insert(30)

assert tree.root.value == 20
assert tree.inorder() == [10, 20, 30]


# LR rotation
tree = AVL()

tree.insert(30)
tree.insert(10)
tree.insert(20)

assert tree.root.value == 20
assert tree.inorder() == [10, 20, 30]


# RL rotation
tree = AVL()

tree.insert(10)
tree.insert(30)
tree.insert(20)

assert tree.root.value == 20
assert tree.inorder() == [10, 20, 30]


# Search
tree = AVL()

for value in [20, 10, 30, 5, 15, 25, 40]:
    tree.insert(value)

assert tree.search(15) is True
assert tree.search(40) is True
assert tree.search(100) is False


# Delete leaf
tree.delete(5)

assert tree.search(5) is False
assert tree.inorder() == [10, 15, 20, 25, 30, 40]


# Delete node with one child
tree.delete(10)

assert tree.search(10) is False
assert tree.inorder() == [15, 20, 25, 30, 40]


# Delete node with two children
tree.delete(30)

assert tree.search(30) is False
assert tree.inorder() == [15, 20, 25, 40]


# Delete root
tree.delete(20)

assert tree.search(20) is False
assert tree.inorder() == [15, 25, 40]


# Duplicate is ignored
tree = AVL()

tree.insert(10)
tree.insert(10)

assert tree.inorder() == [10]
