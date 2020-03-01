class Solution:
    def searchInsert(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = 0
        reduce = False

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
                reduce = True
            else:
                lo = mid + 1
                reduce = False

        return mid if reduce else mid + 1


s = Solution()
print(s.searchInsert([1, 3, 5, 6],2))
