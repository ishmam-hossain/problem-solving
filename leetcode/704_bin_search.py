class Solution:
    def search(self, nums, target: int) -> int:
        low = 0
        hi = len(nums) - 1

        while low <= hi:
            mid = (low + hi) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                hi = mid - 1
        else:
            return -1


s = Solution()
# print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1, 0, 3, 5, 9, 12], 2))
