"""
Unit tests for binary_search_tree
"""

import unittest
import binary_search_tree


class BSTNodeTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = binary_search_tree.BSTNode(7)

    def tearDown(self):
        self.SUT = None

    def test_value_set(self):
        self.assertEqual(self.SUT.val, 7)


class BinarySearchTreeTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = binary_search_tree.BinarySearchTree([4, 1, 6, 0, 12, 7, 13, 5])

    def tearDown(self):
        self.SUT = None

    def test_count(self):
        self.assertEqual(self.SUT.count(), 8)

    def test_root(self):
        self.assertEqual(self.SUT.root().val, 4)

    def test_contains(self):
        self.assertEqual(self.SUT.contains(1), True)
        self.assertEqual(self.SUT.contains(9999), False)

    def test_clear(self):
        self.SUT.clear()
        self.assertEqual(self.SUT.count(), 0)
        self.assertRaises(ValueError, self.SUT.root)

    def test_to_array(self):
        self.assertEqual(self.SUT.to_array(), [4, 1, 6, 0, 5, 12, 7, 13])

    def test_insert(self):
        pass

    def test_remove(self):
        pass

if __name__ == '__main__':
    unittest.main()
