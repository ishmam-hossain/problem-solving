class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, n in enumerate(prices[:-1]):
            if n < prices[i + 1]:
                max_profit += prices[i + 1] - n

        return max_profit
