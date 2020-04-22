class Solution:
    def subarraySum(self, nums, k: int) -> int:
        count, cur, res = {0: 1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res


s = Solution()
print(s.subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
print(s.subarraySum([1, 1, 1], 2))
