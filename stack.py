"""Stack LIFO"""

import doubly_linked_list


class Stack:
    def __init__(self, array=None):
        self.linked_list = doubly_linked_list.DoublyLinkedList(array)

    def __iter__(self):
        pass

    def __str__(self):
        return str(self.linked_list)

    def push(self, val):
        self.linked_list.add(val)

    def pop(self):
        if self.count() == 0:
            raise ValueError("queue is empty")

        val = self.linked_list.last_node.val
        self.linked_list.remove_last()
        return val

    def peek(self):
        if self.count() == 0:
            raise ValueError("queue is empty")

        return self.linked_list.last_node.val

    def count(self):
        return self.linked_list.count()


if __name__ == "__main__":
    stack = Stack([1, 2, 3, 4, 5])
    # print(stack.count())
    # print(stack)
    # print(stack.pop())
    # # print(stack.count())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack)
    # print("count" + str(stack.count()))
    # print(stack.pop())
    # print(stack.peek())
    # print("count" + str(stack.count()))

