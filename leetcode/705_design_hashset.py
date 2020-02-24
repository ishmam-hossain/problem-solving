from collections import deque


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = deque()

    def add(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)
        self.hash_set.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hash_set


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
# obj.remove(1)
param_3 = obj.contains(1)
print(param_3)

