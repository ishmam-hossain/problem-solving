from random import randint


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.hash.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        try:
            self.hash.remove(val)
            return True
        except ValueError:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        index = randint(0, len(self.hash) - 1)
        return self.hash[index]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()