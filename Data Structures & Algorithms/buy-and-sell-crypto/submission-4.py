class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyday = prices[0]
        profit = 0
        n = len(prices)
        for i in range(n):
            buyday = min(buyday,prices[i])
            profit = max(profit,prices[i]-buyday)

        return profit

            