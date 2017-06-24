"""
Implementation of custom hash_map

allows to get item by key in O(1) complexity
in this case worst complexity will be bigger as it doesn't support array resize which
cause lots of collisions if capacity has been chosen wrong
"""


class HashMap:
    def __init__(self, capacity=16):
        if capacity < 1:
            raise ValueError("capacity can't be less then 1")

        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        String representation

        ex: {'some_key_1': 'some_val_1', 'some_key_2': 'some_val_2'}
        """

        result = ""

        for i, pair in enumerate(self):
            result += f"'{pair[0]}':'{pair[1]}'{', ' if i < self.size-1 else ''}"

        return f"{{{result}}}"

    def __getitem__(self, key):
        """
        Indexer

        ex: h_map["some_key_1"]
        """

        return self.get(key)

    def __iter__(self):
        """Items Iterator"""

        return self.items()

    def get(self, key, def_value=None):
        """Get item by key"""

        index = self._get_hash(key)

        if self.table[index] is not None:
            for pair in self.table[index]:
                if key == pair[0]:
                    return pair[1]

        if def_value is not None:
            return def_value

        raise ValueError(f"can't find value with given key {key}")

    def update(self, key, val):
        """Update item"""

        index = self._get_hash(key)

        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = val
                    return

        raise ValueError(f"can't find key {key}")

    def add(self, key, val):
        """Add item"""

        index = self._get_hash(key)
        key_val = [key, val]

        if self.table[index] is None:
            # create new key-value collection
            self.table[index] = list([key_val])
        else:
            # override value for the same key
            for pair in self.table[index]:
                if pair[0] == key:
                    raise ValueError(f"duplicate key {key}")

            # append key-value collection
            self.table[index].append(key_val)

        self.size += 1

    def remove(self, key):
        """Remove item by key"""

        index = self._get_hash(key)

        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if key == pair[0]:
                    del self.table[index][i]
                    self.size -= 1
                    return

        raise ValueError(f"can't find value with given key {key}")

    def empty(self):
        return self.size == 0

    def count(self):
        """Count"""

        return self.size

    def contains(self, key):
        """Checks if the key is in the hashmap"""

        return key in self.keys()

    def keys(self):
        """Returns keys generator"""

        for items in self.table:
            if items is not None:
                for pair in items:
                    yield pair[0]

    def values(self):
        """Returns values generator"""

        for items in self.table:
            if items is not None:
                for pair in items:
                    yield pair[1]

    def items(self):
        """Returns items generator"""

        for items in self.table:
            if items is not None:
                for pair in items:
                    yield pair

    def _get_hash(self, key):
        # should be more complicated
        _hash = 0

        for char in str(key):
            _hash += ord(char)

        return _hash % self.capacity


if __name__ == "__main__":
    pass
    # hash_map = HashMap()
    # hash_map.add("test1", "apple")
    # hash_map.add("test2", "orange")
    # hash_map.add("test11", "grape")
    # hash_map.add("test111", "kiwi")
    # hash_map.add("test5", "apple_new")

    # print(hash_map)
    # print(list(hash_map.keys()))
    # print(*hash_map.values())
    # print(*hash_map.items())
    # print(hash_map.table)
    # print(hash_map.get("test1"))
    # print(hash_map.get("xxxxxxxx", "my def value"))
    # print(hash_map.remove("test1"))
    # print(hash_map.table)
    #

    # for k in hash_map.keys():
    #     print(f"key: {k}")
    #
    # for k, v in hash_map:
    #     print(f"key: {k}, val: {v}")
    #
    # print(hash_map)
    # print(hash_map['test2'])
