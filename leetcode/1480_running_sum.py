class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        running_sum = 0
        for i, n in enumerate(nums):
            running_sum += n
            res[i] = running_sum

        return res

    def runningSumBetter(self, nums: List[int]) -> List[int]:
        running_sum = 0
        for i, n in enumerate(nums):
            running_sum += n
            nums[i] = running_sum

        return nums




