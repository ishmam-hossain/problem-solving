class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 1
        for i in range(1, len(nums), 1):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1

        return nums


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(s.removeDuplicates([1, 1, 2]))
