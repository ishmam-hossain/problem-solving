class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) > 1:
            stones.sort()

            new = abs(stones[-1] - stones[-2])

            if new > 0:
                stones[-2] = new
            else:
                stones.pop()
            stones.pop()

        return stones[0] if stones else 0
