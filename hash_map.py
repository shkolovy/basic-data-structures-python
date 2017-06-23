"""Implementation of custom hash_map"""


class HashMap:
    def __init__(self):
        self.map_size = 6
        self.map = [None] * self.map_size
        self.size = 0

    def __str__(self):
        result = "{"

        for i, pair in enumerate(self):
            result += f"'{pair[0]}':'{pair[1]}'"
            if i < self.size-1:
                result += ", "

        result += "}"
        return result

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        for item in self.map:
            if item is not None:
                for pair in item:
                    yield pair

    def get(self, key, def_value=None):
        """Get item by key"""

        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if key == pair[0]:
                    return pair[1]

        if def_value is not None:
            return def_value

        raise ValueError(f"can't find value with given key {key}")

    def add(self, key, val):
        """Add or update item"""

        key_hash = self._get_hash(key)
        key_val = [key, val]

        if self.map[key_hash] is None:
            # can be linked list
            # create new key-value collection
            self.map[key_hash] = list([key_val])
            self.size += 1
            return
        else:
            # override value for the same key
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = val
                    return

            # append key-value collection
            self.map[key_hash].append(key_val)
            self.size += 1

    def remove(self, key):
        """Remove item by key"""

        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for i, pair in enumerate(self.map[key_hash]):
                if key == pair[0]:
                    del self.map[key_hash][i]
                    self.size -= 1
                    return

        raise ValueError(f"can't find value with given key {key}")

    def count(self):
        return self.size

    def contains(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return True

        return False

    def _get_hash(self, key):
        # should be more complicated
        _hash = 0

        for char in str(key):
            _hash += ord(char)

        return _hash % self.map_size


if __name__ == "__main__":
    hash_map = HashMap()
    hash_map.add("test1", "apple")
    hash_map.add("test2", "orange")
    hash_map.add("test11", "grape")
    hash_map.add("test111", "kiwi")
    hash_map.add("test1", "apple_new")

    print(hash_map.map)
    print(hash_map.get("test1"))
    print(hash_map.get("xxxxxxxx", "my def value"))
    print(hash_map.remove("test1"))
    print(hash_map.map)

    for key, val in hash_map:
        print(f"key: {key}, val: {val}")

    print(hash_map)
    print(hash_map['test2'])
