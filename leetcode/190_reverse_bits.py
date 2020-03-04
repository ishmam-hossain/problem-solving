from collections import deque


class Solution:
    def reverseBits(self, n: int) -> int:
        _sum = 0
        i = 0
        q = deque()

        while n:
            digit = n % 10
            n //= 10
            q.append(digit)
            i += 1

        while i != 32:
            q.append(0)
            i += 1

        while q:
            digit = q.popleft()
            _sum += digit * 2 ** i

        return _sum


s = Solution()
print(s.reverseBits(10100101000001111010011100))
