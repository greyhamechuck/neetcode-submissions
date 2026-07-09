class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        n = len(prices)
        right = 0
        result = 0
        while right < n:
            if prices[right]< prices[left]:
                left = right
            else:
                price = prices[right] - prices[left]
                result = max(result,price)
            right +=1
        return result