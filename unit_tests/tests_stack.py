"""
Unit tests for stack
"""

import unittest
import stack


class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = stack.Stack([4, 1, 6, 0, 12, 7, 13, 5])

    def tearDown(self):
        self.SUT = None

    def test_count(self):
        self.assertEqual(self.SUT.count(), 8)

    def test_push(self):
        self.SUT.push(12)
        self.assertEqual(self.SUT.count(), 9)

    def test_peek(self):
        self.assertEqual(self.SUT.peek(), 5)

    def test_pop(self):
        self.assertEqual(self.SUT.pop(), 5)
        self.assertEqual(self.SUT.count(), 7)

    def test_empty(self):
        self.assertEqual(self.SUT.empty(), False)


if __name__ == '__main__':
    unittest.main()
