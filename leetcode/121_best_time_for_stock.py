class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        min_amt = 999999999999999
        for i, n in enumerate(prices):
            if n < min_amt:
                min_amt = n
            else:
                max_profit = max(max_profit, n - min_amt)

        return max_profit


s = Solution()
print(s.maxProfit([1,2,3,4,5,6]))
