"""
Unit tests for linked_list
"""

import unittest
import linked_list


class LLNodeTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = linked_list.LLNode(7)

    def tearDown(self):
        self.SUT = None

    def test_value_set(self):
        self.assertEqual(self.SUT.val, 7)


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = linked_list.LinkedList([4, 1, 6, 0, 12, 7, 13, 5])

    def tearDown(self):
        self.SUT = None

    def test_count(self):
        self.assertEqual(self.SUT.count(), 8)

    def test_contains(self):
        self.assertEqual(self.SUT.contains(1), True)

    def test_clear(self):
        self.SUT.clear()
        self.assertEqual(self.SUT.count(), 0)

    def test_to_array(self):
        self.assertEqual(self.SUT.to_array(), [4, 1, 6, 0, 12, 7, 13, 5])

    def test_add(self):
        self.SUT.add(12)
        self.assertEqual(self.SUT.contains(12), True)
        self.assertEqual(self.SUT.count(), 9)

    def test_remove_first(self):
        self.SUT.remove(4)
        self.assertEqual(self.SUT.count(), 7)
        self.assertEqual(self.SUT.to_array(), [1, 6, 0, 12, 7, 13, 5])

    def test_remove_last(self):
        self.SUT.remove(5)
        self.assertEqual(self.SUT.count(), 7)
        self.assertEqual(self.SUT.to_array(), [4, 1, 6, 0, 12, 7, 13])

    def test_remove_middle(self):
        self.SUT.remove(0)
        self.assertEqual(self.SUT.count(), 7)
        self.assertEqual(self.SUT.to_array(), [4, 1, 6, 12, 7, 13, 5])


if __name__ == '__main__':
    unittest.main()
