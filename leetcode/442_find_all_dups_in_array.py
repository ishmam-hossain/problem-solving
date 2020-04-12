class Solution:
    def findDuplicates(self, nums):
        dups = []

        for n in nums:
            if nums[abs(n)-1] < 0:
                dups.append(abs(n))

            else:
                nums[abs(n) - 1] = -abs(nums[abs(n)-1])
        return dups


s = Solution()
print(s.findDuplicates([2, 2]))
print(s.findDuplicates([4,3,2,7,8,2,3,1]))
