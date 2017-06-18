"""Binary tree module"""


class BSTNode:
    """
    Node obj

    val: node value
    left: left node
    right: right node
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'node value: {self.val}'


class BinarySearchTree:
    """Binary Search Tree"""

    def __init__(self, array=None):
        self.root_node = None
        self.size = 0

        # add nodes from array
        if array is not None:
            for val in array:
                self.insert(val)

    def __str__(self):
        return str(self.to_array())

    def insert(self, val):
        """Add new node"""

        if self.root_node is None:
            self.root_node = BSTNode(val)
        else:
            self._insert(self.root_node, val)

        self.size += 1

    def _insert(self, node, val):
        if node.val == val:
            raise ValueError(f"duplicate value {val}")

        if node.val < val:
            if node.right is None:
                node.right = BSTNode(val)
            else:
                self._insert(node.right, val)
        else:
            if node.left is None:
                node.left = BSTNode(val)
            else:
                self._insert(node.left, val)

    def contains(self, val):
        """Find node by value"""

        current_node = self.root_node

        while current_node is not None:
            if current_node.val == val:
                return True
            elif current_node.val < val:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return False

    def remove(self, val):
        """Remove node"""

        current_node = self.root_node
        parent_node = None
        node_to_remove = None

        while current_node is not None:
            if current_node.val == val:
                node_to_remove = current_node
                break
            elif current_node.val < val:
                parent_node = current_node
                current_node = current_node.right
            else:
                parent_node = current_node
                current_node = current_node.left

        if node_to_remove is None:
            raise ValueError(f"can't find node to remove {val}")

        # node has no children
        if node_to_remove.left is None and node_to_remove.right is None:
            parent_node.left = None
            parent_node.right = None
            self.size -= 1
            return

        # node has one child
        if node_to_remove.left is None or node_to_remove.right is None:
            if parent_node.left is node_to_remove:
                parent_node.left = node_to_remove.left if node_to_remove.left is not None else node_to_remove.right
            else:
                parent_node.right = node_to_remove.left if node_to_remove.left is not None else node_to_remove.right
            self.size -= 1
            return

    def clear(self):
        """Remove all nodes"""

        self.root_node = None
        self.size = 0

    def to_array(self):
        """Returns tree in array representation"""

        if self.root_node is None:
            return []

        ar = []

        self._append_array(self.root_node, ar)

        return ar

    def _append_array(self, node, ar):
        if node is not None:
            ar.append(node.val)

            if node.left is not None:
                self._append_array(node.left, ar)
            if node.right is not None:
                self._append_array(node.right, ar)

    def print(self, node):
        pass

    def root(self):
        """Root node"""
        if self.root_node is None:
            raise ValueError("no root node")

        return self.root_node

    def count(self):
        """Number of nodes"""

        return self.size


if __name__ == "__main__":
    some_values = [4, 1, 6, 0, 12, 7, 13, 5]
    bst_tree = BinarySearchTree(some_values)

    print(f"root - {bst_tree.root()}")
    print(f"number of nodes - {bst_tree.count()}")
    print(f"found - {bst_tree.contains(1)}")
    print(bst_tree.count())
    print(bst_tree.to_array())
    bst_tree.insert(44)
    bst_tree.insert(23)
    print(f"number of nodes - {bst_tree.count()}")
    print(bst_tree)
    bst_tree.remove(44)
    bst_tree.remove(1)
    print(bst_tree)

