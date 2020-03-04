class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        """
            O(n^2) solution.
            TLE khabo sure :3
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and abs(i - j) <= k and nums[i] ^ nums[j] == 0:
                    return True

        return False

    def not_optimized(self, nums, k):
        for i, n in enumerate(nums):
            for j in range(i+1, i+k+1):
                if abs(j-i) <=k and j < len(nums):
                    if nums[i] ^ nums[j] == 0:
                        return True
        return False

    def most_optimized(self, nums, k):
        occurred_at = {}
        for i, n in enumerate(nums):
            if n in occurred_at:
                if i - occurred_at.get(n) <= k:
                    return True
            occurred_at[n] = i
        return False


s = Solution()
print(s.most_optimized([1,2,3,1], 3))
