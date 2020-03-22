class Solution:
    def createTargetArray(self, nums, index):
        target = []

        for n, i in zip(nums, index):
            target.insert(i, n)
        return target


s = Solution()
print(s.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
