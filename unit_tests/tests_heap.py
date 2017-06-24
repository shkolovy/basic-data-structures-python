"""
Unit tests for heap
"""

import unittest
import heap


class HeapTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = heap.Heap()
        self._add_items()

    def tearDown(self):
        self.SUT = None

    def test_count(self):
        self.assertEqual(self.SUT.count(), 6)

    def test_empty(self):
        self.SUT.clear()
        self.assertEqual(self.SUT.count(), 0)

    def test_add(self):
        self.SUT.add(30)
        self.assertEqual(self.SUT.items[0], 30)
        self.SUT.add(29)
        self.assertEqual(self.SUT.items[1], 29)

    def test_peek(self):
        self.assertEqual(self.SUT.peek(), 12)

    def test_remove_max(self):
        self.assertEqual(self.SUT.remove_max(), 12)
        self.assertEqual(self.SUT.count(), 5)
        self.assertEqual(self.SUT.peek(), 8)
        self.assertEqual(self.SUT.remove_max(), 8)
        self.assertEqual(self.SUT.peek(), 3)

    def _add_items(self):
        self.SUT.add(2)
        self.SUT.add(8)
        self.SUT.add(3)
        self.SUT.add(1)
        self.SUT.add(12)
        self.SUT.add(0)


if __name__ == '__main__':
    unittest.main()
