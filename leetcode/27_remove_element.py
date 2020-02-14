class Solution:
    def removeElement(self, nums, val: int) -> int:
        removal_indexes = []
        count = 0
        for i, n in enumerate(nums):
            if n == val:
                nums[i] = None
            else:
                count += 1
                removal_indexes.append(i)

        for i in range(len(nums)):
            if nums[i] is None:
                try:
                    nums[i] = nums[removal_indexes.pop()]
                except IndexError:
                    count = count

        return len(nums[:count])


nums = [2, 2, 3]
val = 2     # ans 5 --> [0, 1, 2, 3, 4]
s = Solution()
# print(nums)
print(s.removeElement(nums, val))
