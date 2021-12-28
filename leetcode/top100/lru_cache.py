import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.mp = collections.OrderedDict()
        self.capacity = capacity

    def get_next_key(self):
        for key in self.mp.keys():
            yield key

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1

        result = self.mp.get(key)

        del self.mp[key]
        self.mp[key] = result

        return result

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            del self.mp[key]
            self.mp[key] = value
        else:
            if len(self.mp) == self.capacity:
                del self.mp[next(self.get_next_key())]

            self.mp[key] = value


if __name__ == "__main__":
    # ["LRUCache","put","get","put","get","get"]
    # [[1],[2,1],[2],[3,2],[2],[3]]

    cache = LRUCache(1)

    cache.put(2, 1)

    assert cache.get(2) == 1

    cache.put(3, 2)

    assert cache.get(2) == -1

    assert cache.get(3) == 2


    print("=============Example 2============")

    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    cache = LRUCache(2)

    cache.put(1, 1)

    cache.put(2, 2)

    assert cache.get(1) == 1

    cache.put(3, 3)

    assert cache.get(2) == -1

    cache.put(4, 4)

    assert cache.get(1) == -1

    # ["LRUCache","get","put","get","put","put","get","get"]
    # [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

    print("=====Example 3======")

    cache = LRUCache(2)

    assert cache.get(2) == -1

    cache.put(2, 6)

    assert cache.get(1) == -1

    cache.put(1, 5)

    cache.put(1, 2)

    assert cache.get(1) == 2

    assert cache.get(2) == 6

    # ["LRUCache", "put", "put", "put", "put", "get", "get", "get", "get", "put", "get", "get", "get", "get", "get"]
    # [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]]

    print("====example 4====")
    cache = LRUCache(3)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)

    cache.put(4, 4)

    assert cache.get(4) == 4
