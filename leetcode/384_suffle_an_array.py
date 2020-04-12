from random import randint


class Solution:

    def __init__(self, nums):
        self.actual = nums
        self.shuffled = random.sample(self.actual, len(self.actual))

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.shuffled = self.actual[:]
        return self.shuffled

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        return random.sample(self.shuffled, len(self.shuffled))

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()