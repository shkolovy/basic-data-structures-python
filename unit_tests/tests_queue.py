"""
Unit tests for queue
"""

import unittest
import queue


class QueueTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = queue.Queue([4, 1, 6, 0, 12, 7, 13, 5])

    def tearDown(self):
        self.SUT = None

    def test_count(self):
        self.assertEqual(self.SUT.count(), 8)

    def test_enqueue(self):
        self.SUT.enqueue(6)
        self.assertEqual(self.SUT.count(), 9)

    def test_peek(self):
        self.assertEqual(self.SUT.peek(), 4)

    def test_dequeue(self):
        self.assertEqual(self.SUT.dequeue(), 4)
        self.assertEqual(self.SUT.count(), 7)

    def test_empty(self):
        self.assertEqual(self.SUT.empty(), False)


if __name__ == '__main__':
    unittest.main()
