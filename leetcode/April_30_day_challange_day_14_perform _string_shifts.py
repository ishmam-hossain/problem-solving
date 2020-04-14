from collections import deque


class Solution:
    def stringShift(self, s: str, shift) -> str:
        d = deque(s)

        for direction, amt in shift:
            if direction == 0:
                for a in range(amt):
                    d.append(d.popleft())
            else:
                for a in range(amt):
                    d.appendleft(d.pop())

        return "".join(d)


s = Solution()
print(s.stringShift("abc", [[0, 1], [1, 2]]))
