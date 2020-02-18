class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n != 1:
            if n in visited:
                return False
            visited.append(n)
            cur = n
            _sum = 0
            while cur:
                _sum += (cur % 10) ** 2
                cur = cur // 10
            n = _sum
        return True


s = Solution()
print(s.isHappy(9))
