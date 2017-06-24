"""
Unit tests for hash map
"""

import unittest
import hash_map


class HashMapTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = hash_map.HashMap()

    def tearDown(self):
        self.SUT = None

    def _add_items(self):
        self.SUT.add("key1", "val1")
        self.SUT.add("key2", "val2")
        self.SUT.add("key3", "val3")

    def test_count(self):
        self._add_items()
        self.assertEqual(self.SUT.count(), 3)

    def test_empty(self):
        self.assertEqual(self.SUT.empty(), True)

    def test_keys(self):
        self._add_items()
        self.assertEqual(list(self.SUT.keys()), ["key1", "key2", "key3"])

    def test_values(self):
        self._add_items()
        self.assertEqual(list(self.SUT.values()), ["val1", "val2", "val3"])

    def test_contains(self):
        self._add_items()
        self.assertEqual(self.SUT.contains("key1"), True)
        self.assertEqual(self.SUT.contains("key4"), False)

    def test_get(self):
        self._add_items()
        self.assertEqual(self.SUT.get("key1"), "val1")
        self.assertEqual(self.SUT.get("key44", "val_def"), "val_def")
        self.assertRaises(ValueError, self.SUT.get, "xxx")

    def test_update(self):
        self._add_items()
        self.SUT.update("key1", "val1_updated")
        self.assertEqual(self.SUT.get("key1"), "val1_updated")

    def test_add(self):
        self._add_items()
        self.SUT.add("key4", "val4")
        self.assertEqual(self.SUT.count(), 4)
        self.assertEqual(self.SUT.get("key4"), "val4")

    def test_remove(self):
        self._add_items()
        self.SUT.remove("key1")
        self.assertEqual(self.SUT.count(), 2)
        self.assertEqual(self.SUT.get("key", "def"), "def")

    def test_opacity(self):
        self.SUT = hash_map.HashMap(4)
        self.assertEqual(self.SUT.capacity, 4)

if __name__ == '__main__':
    unittest.main()
