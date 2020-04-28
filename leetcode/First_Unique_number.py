from collections import deque


class FirstUnique:

    def __init__(self, nums):
        self.q = deque()
        self.seen = set()

        for n in nums:
            if n not in self.seen:
                self.q.append(n)
                self.seen.add(n)
            else:
                try:
                    self.q.remove(n)
                except ValueError:
                    pass

    def showFirstUnique(self) -> int:
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if value not in self.seen:
            self.q.append(value)
            self.seen.add(value)
        else:
            try:
                self.q.remove(value)
            except ValueError:
                pass


# Your FirstUnique object will be instantiated and called as such:
nums = [1, 4, 2, 4, 6, 3, 2, 6, 2, 4, 7, 8, 7]
obj = FirstUnique(nums)
print(obj.q)

print(obj.showFirstUnique())
obj.add(1)
print(obj.q)
print(obj.showFirstUnique())

