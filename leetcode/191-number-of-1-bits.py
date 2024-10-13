class Solution:
    def hammingWeight(self, n: int) -> int:
        set_count = 0

        while n:
            set_count += (n % 2)
            n = n // 2
        
        return set_count
