class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr, temp, maxProfit = prices[0], 0, 0
        for i in range(len(prices)):
            if prices[i] < curr:
                maxProfit = max(maxProfit, temp)
                temp = 0
                curr = prices[i]
                continue
            temp = max(temp, prices[i] - curr)
        return max(maxProfit, temp)
