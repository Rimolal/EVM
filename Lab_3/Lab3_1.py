from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            r += 1
        return max_profit

prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))
        