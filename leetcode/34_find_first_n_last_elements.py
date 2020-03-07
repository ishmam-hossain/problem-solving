class Solution:
    def searchRange(self, nums, target: int):
        first = self.bin_search(nums, target, True)
        last = self.bin_search(nums, target)

        return [first, last]

    def bin_search(self, nums, target, is_first=False):
        lo = 0
        hi = len(nums) - 1
        res = -1
        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                res = mid
                if is_first:
                    hi = mid - 1
                else:
                    lo = mid + 1

            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return res


s = Solution()
print(s.searchRange([1, 2, 2, 3, 4, 5, 6], 7))
