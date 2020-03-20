class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = [-1] * 100000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.vals[key - 1] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.vals[key - 1]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.vals[key - 1] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)