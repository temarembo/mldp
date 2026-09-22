class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def merge_with_dummy(list1: Node | None, list2: Node | None) -> Node | None:
    dummy = Node(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


def merge_without_dummy(list1: Node | None, list2: Node | None) -> Node | None:
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.value <= list2.value:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    tail = head

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return head


def build_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    tail = head

    for value in values[1:]:
        tail.next = Node(value)
        tail = tail.next

    return head


def linked_list_to_list(head):
    result = []

    while head is not None:
        result.append(head.value)
        head = head.next

    return result


def test_merge(merge_function):
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    result = merge_function(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]

    list1 = build_linked_list([])
    list2 = build_linked_list([])
    result = merge_function(list1, list2)
    assert linked_list_to_list(result) == []

    list1 = build_linked_list([])
    list2 = build_linked_list([1, 2, 3])
    result = merge_function(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3]

    list1 = build_linked_list([1, 2, 3])
    list2 = build_linked_list([])
    result = merge_function(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3]

    list1 = build_linked_list([1])
    list2 = build_linked_list([2])
    result = merge_function(list1, list2)
    assert linked_list_to_list(result) == [1, 2]

    list1 = build_linked_list([5, 6])
    list2 = build_linked_list([1, 2, 3])
    result = merge_function(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 5, 6]

    list1 = build_linked_list([1, 3, 5])
    list2 = build_linked_list([2, 4, 6])
    result = merge_function(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]

    list1 = build_linked_list([1, 1, 3])
    list2 = build_linked_list([1, 2, 2])
    result = merge_function(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 1, 2, 2, 3]


test_merge(merge_with_dummy)
test_merge(merge_without_dummy)
