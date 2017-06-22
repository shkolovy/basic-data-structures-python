"""Queue FIFO"""

import doubly_linked_list


class Queue:
    def __init__(self, array=None):
        self.linked_list = doubly_linked_list.DoublyLinkedList(array)

    def __iter__(self):
        return iter(self.linked_list)

    def __str__(self):
        return str(self.linked_list)

    def enqueue(self, val):
        """Put value into the queue"""

        self.linked_list.add(val)

    def dequeue(self):
        """Return and delete current value"""

        if self.count() == 0:
            raise ValueError("queue is empty")

        val = self.linked_list.root_node.val
        self.linked_list.remove_first()
        return val

    def peek(self):
        """Return current value without deleting"""

        if self.count() == 0:
            raise ValueError("queue is empty")

        return self.linked_list.root_node.val

    def count(self):
        """Count"""

        return self.linked_list.count()

    def empty(self):
        """Is empty"""

        return self.count() == 0

if __name__ == "__main__":
    pass

