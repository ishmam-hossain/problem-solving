class Solution:
    def search(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        rotate = lo
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mid = (lo + hi) // 2
            real_mid = (mid+rotate) % len(nums)

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 5))
