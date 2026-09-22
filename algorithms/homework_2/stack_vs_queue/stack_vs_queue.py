class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        head = self.head

        if head is None:
            return None

        self.head = head.next
        return head.value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        head = self.head

        if head is None:
            return None

        self.head = head.next

        if self.head is None:
            self.tail = None

        return head.value


# Stack

stack = Stack()

# Пустой стек
assert stack.pop() is None

# Добавление одного элемента
stack.push(10)
assert stack.pop() == 10

# Проверка порядка LIFO
stack.push(10)
stack.push(20)
stack.push(30)

assert stack.pop() == 30
assert stack.pop() == 20
assert stack.pop() == 10

# После удаления всех элементов стек снова пуст
assert stack.pop() is None


# Queue

queue = Queue()

# Пустая очередь
assert queue.dequeue() is None

# Добавление одного элемента
queue.enqueue(10)
assert queue.dequeue() == 10

# После удаления последнего элемента обе ссылки должны быть пустыми
assert queue.head is None
assert queue.tail is None

# Проверка порядка FIFO
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

assert queue.dequeue() == 10
assert queue.dequeue() == 20
assert queue.dequeue() == 30

# Очередь снова пустая
assert queue.dequeue() is None
assert queue.head is None
assert queue.tail is None
