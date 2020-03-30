class Solution:
    def checkPossibility(self, nums) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            diff = nums[i+1]-nums[i]
            count += diff
            print(count)
        return 0 <= abs(count) <= 1


s = Solution()
print(s.checkPossibility([3, 4, 2, 3]))
# print(s.checkPossibility([1, 2, 3]))
# print(s.checkPossibility([4, 2, 3]))



"""
        count = 0
        for i in range(len(nums) - 2):
            if nums[i] > nums[i + 1]:
                count += 1
                nums[i+1] = nums[i]
        count += 1 if nums[-2] > nums[-1] else 0
        return count <= 1
"""