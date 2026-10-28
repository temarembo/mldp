class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._rec_insert(self.root, value)
        return self.root

    def _rec_insert(self, root, value):
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self._rec_insert(root.left, value)
        else:
            root.right = self._rec_insert(root.right, value)

        return root

    def preorder(self):
        result = []
        return self._preorder(self.root, result)

    def _preorder(self, root, result):
        if not root:
            return result

        result.append(root.value)
        self._preorder(root.left, result)
        self._preorder(root.right, result)

        return result

    def inorder(self):
        result = []
        return self._inorder(self.root, result)

    def _inorder(self, root, result):
        if not root:
            return result

        self._inorder(root.left, result)
        result.append(root.value)
        self._inorder(root.right, result)

        return result

    def postorder(self):
        result = []
        return self._postorder(self.root, result)

    def _postorder(self, root, result):
        if not root:
            return result

        self._postorder(root.left, result)
        self._postorder(root.right, result)
        result.append(root.value)

        return result

    def reverse_preorder(self):
        result = []
        return self._reverse_preorder(self.root, result)

    def _reverse_preorder(self, root, result):
        if not root:
            return result

        result.append(root.value)
        self._reverse_preorder(root.right, result)
        self._reverse_preorder(root.left, result)

        return result

    def reverse_inorder(self):
        result = []
        return self._reverse_inorder(self.root, result)

    def _reverse_inorder(self, root, result):
        if not root:
            return result

        self._reverse_inorder(root.right, result)
        result.append(root.value)
        self._reverse_inorder(root.left, result)

        return result

    def reverse_postorder(self):
        result = []
        return self._reverse_postorder(self.root, result)

    def _reverse_postorder(self, root, result):
        if not root:
            return result

        self._reverse_postorder(root.right, result)
        self._reverse_postorder(root.left, result)
        result.append(root.value)

        return result
