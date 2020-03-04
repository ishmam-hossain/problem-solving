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

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in nums2:
            index = self.searchInsert(nums1[:m + 1], x)
            if index <= m:
                nums1[index + 1:m + 1] = nums1[index:m]
                nums1[index] = x
            else:
                nums1[m] = x
            m += 1
