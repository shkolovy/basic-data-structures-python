"""
Heap

binary tree, parent always bigger then children
add elements from left to right

heap example:

     8
  6     5
3  4  2

array representation:
[8, 6, 5, 3, 4, 2]

root item always MAX item

get left child
index * 2 + 1

get right child
index * 2 + 2

get parent
floor (index - 1) / 2
"""


class Heap:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def add(self, val):
        """Add item to the heap"""

        self.items.append(val)

        current_item_index = len(self.items) - 1
        current_parent_index = self._get_parent_index(current_item_index)

        while current_item_index > 0 and self.items[current_parent_index] < self.items[current_item_index]:
            self._swap(current_item_index, current_parent_index)

            current_item_index = current_parent_index
            current_parent_index = self._get_parent_index(current_item_index)

    def peek(self):
        """Return max item"""

        if self.empty():
            raise ValueError("heap is empty")

        return self.items[0]

    def remove_max(self):
        """Remove max element from the heap and return it"""

        if self.empty():
            raise ValueError("heap is empty")

        max_item = self.items[0]
        # put the latest item to the root

        self.items[0] = self.items[len(self.items) - 1]
        del self.items[len(self.items) - 1]

        current_index = 0

        while current_index < self.count():
            left_index = current_index * 2 + 1
            right_index = current_index * 2 + 2

            if left_index >= self.count():
                # out of heap
                break

            max_child_index = self._get_max_child_index(left_index, right_index)

            self._swap(current_index, max_child_index)

            current_index = max_child_index

        return max_item

    def count(self):
        """Count of elements"""

        return len(self.items)

    def clear(self):
        """Clear the heap"""

        self.items = []

    def empty(self):
        """Is empty"""

        return self.count() == 0

    def _get_max_child_index(self, left_index, right_index):
        if right_index >= self.count():
            # out of heap
            max_child_index = left_index
        elif self.items[left_index] > self.items[right_index]:
            max_child_index = left_index
        else:
            max_child_index = right_index

        return max_child_index

    def _swap(self, index1, index2):
        val1 = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = val1

    @staticmethod
    def _get_parent_index(index):
        return int((index - 1) / 2)


if __name__ == "__main__":
    pass
    # heap = Heap()
    # heap.add(2)
    # heap.add(4)
    # heap.add(1)
    # heap.add(7)
    # heap.add(0)
    # heap.add(12)
    #
    # print(heap.remove_max())
    # print(heap)
