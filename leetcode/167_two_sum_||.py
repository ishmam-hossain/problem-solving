class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            compliment = self.bin_search(numbers, target - n)
            if 0 <= compliment != i:
                return sorted([i + 1, compliment + 1])

    def bin_search(self, nums, target):
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1
