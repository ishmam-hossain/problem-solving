from random import randint


class Solution:

    def __init__(self, nums):
        self.actual = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.actual

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        length = len(self.actual)
        res = self.actual[:]
        if length > 1:
            for i in range(randint(1, length)):
                res[i], res[length-1-i] = res[length-1-i], res[i]

        return res


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5, 6]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)
