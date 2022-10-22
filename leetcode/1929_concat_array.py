class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        res = [None] * (sz * 2)

        for i, n in enumerate(nums):
            res[i], res[i + sz] = n, n

        return res

    def getConcatenationBetter(self, nums: List[int]) -> List[int]:
        return nums * 2

    def getConcatenationmaybeBetter(self, nums: List[int]) -> List[int]:
        return nums + nums

