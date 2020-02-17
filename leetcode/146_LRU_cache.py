from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        val = self.cache.get(key, None)
        if val:
            pop_val = self.cache.pop(key)
            self.cache[key] = pop_val
        return val if val else -1

    def put(self, key: int, value: int) -> None:
        if self.cache.__len__() + 1 <= self.capacity:
            if key in self.cache:
                self.cache.pop(key)
                self.cache[key] = value
            else:
                self.cache[key] = value
        else:
            if key in self.cache:
                self.cache.pop(key)
                self.cache[key] = value
            else:
                self.cache.pop(self.cache.__iter__().__next__())
                self.cache[key] = value


"""
["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

[null,null,null,null,null,-1,3]

["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

["LRUCache","get","put","get","put","put","get","get"]
[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
[null,-1,null,-1,null,null,2,6]

"""