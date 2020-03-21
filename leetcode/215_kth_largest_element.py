class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        print(nums, -k)
        return nums[-k]


s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
