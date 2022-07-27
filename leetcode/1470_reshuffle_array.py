from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.extend([nums[i], nums[n+i]])
        return res


s = Solution()
res = s.shuffle(nums=[2, 5, 1, 3, 4, 7], n=3)
print("in -> ", [2, 5, 1, 3, 4, 7])
print("out -> ", res)
print("res -> ", [2, 3, 5, 4, 1, 7])
print("-" * 10)
res = s.shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4)
print("in ->", [1, 2, 3, 4, 4, 3, 2, 1])
print("out -> ", res)
print("res -> ", [1, 4, 2, 3, 3, 2, 4, 1])
print("-" * 10)
