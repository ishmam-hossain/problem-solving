class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final = current = 0
        
        for n in nums:
            if n == 1:
                current += 1
                final = max(final, current)
            else:
                current = 0
        
        return final
