class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            cur = n
            _sum = 0
            while cur:
                _sum += (cur % 10) ** 2
                cur = cur // 10
            n = _sum
            visited.add(n)
        return True
