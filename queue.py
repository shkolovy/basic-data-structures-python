"""Queue FIFO"""

import doubly_linked_list


class Queue:
    def __init__(self, array=None):
        self.linked_list = doubly_linked_list.DoublyLinkedList(array)

    def __iter__(self):
        pass

    def __str__(self):
        return str(self.linked_list)

    def enqueue(self, val):
        self.linked_list.add(val)

    def dequeue(self):
        if self.count() == 0:
            raise ValueError("queue is empty")

        val = self.linked_list.root_node.val
        self.linked_list.remove_first()
        return val

    def peek(self):
        if self.count() == 0:
            raise ValueError("queue is empty")

        return self.linked_list.root_node.val

    def count(self):
        return self.linked_list.count()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue)
