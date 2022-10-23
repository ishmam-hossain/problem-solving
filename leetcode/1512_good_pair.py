from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[i + 1:], i + 1):
                count += n1 == n2

        return count

    def numIdenticalPairsBetter(self, nums: List[int]) -> int:
        tracker = dict()
        pairs = 0

        for n in nums:
            pairs += tracker.get(n, 0)
            tracker[n] = tracker.get(n, 0) + 1

        return pairs


s = Solution()
res = s.numIdenticalPairsBetter([1, 2, 3, 1, 1, 3])
print(res)