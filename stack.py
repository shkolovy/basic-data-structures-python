"""Stack LIFO"""

import doubly_linked_list


class Stack:
    def __init__(self, array=None):
        self.linked_list = doubly_linked_list.DoublyLinkedList(array)

    def __iter__(self):
        return iter(self.linked_list)

    def __str__(self):
        return str(self.linked_list)

    def push(self, val):
        """Push value into the Stack"""

        self.linked_list.add(val)

    def pop(self):
        """Return and delete value from the Stack"""

        if self.count() == 0:
            raise ValueError("queue is empty")

        val = self.linked_list.last_node.val
        self.linked_list.remove_last()
        return val

    def peek(self):
        """Return value without deleting"""

        if self.count() == 0:
            raise ValueError("queue is empty")

        return self.linked_list.last_node.val

    def count(self):
        """Count"""

        return self.linked_list.count()

    def empty(self):
        """Is empty"""

        return self.count() == 0

if __name__ == "__main__":
    pass
    # stack = Stack([1, 2, 3, 4, 5, 6])
    #
    # for s in stack:
    #     print(s)
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

