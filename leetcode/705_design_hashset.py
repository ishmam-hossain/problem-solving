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


# a lot faster one
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = [False] * 100000

    def add(self, key: int) -> None:
        self.vals[key - 1] = key

    def remove(self, key: int) -> None:
        self.vals[key - 1] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.vals[key - 1] is False:
            return False
        return True

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

