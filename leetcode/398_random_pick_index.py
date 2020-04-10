from random import randint


class Solution:

    def __init__(self, nums):
        self.holder = {}

        for i, n in enumerate(nums):
            self.holder.setdefault(n, []).append(i)

    def pick(self, target: int) -> int:
        indexes = self.holder[target]
        return indexes[randint(0, len(indexes) - 1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
