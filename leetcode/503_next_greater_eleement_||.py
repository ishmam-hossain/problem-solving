class Solution:
    def nextGreaterElements(self, nums):
        res = []
        for index, n in enumerate(nums):
            i = (index + 1) % len(nums)
            while index != i:
                if nums[i] > n:
                    res.append(nums[i])
                    break
                i = (i + 1) % len(nums)
            else:
                res.append(-1)

        return res


s = Solution()
print(s.nextGreaterElements([1, 2, 1]))
# print(s.nextGreaterElements([100, 1, 11, 1, 120, 111, 123, 1, -1, -100]))  # [120,11,120,120,123,123,-1,100,100,100]
