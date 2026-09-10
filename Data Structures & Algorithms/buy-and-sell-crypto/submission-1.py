class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0

        l = 0
        r = 1
        maxx = 0

        while r < len(prices):
            if prices[r] <= prices[l]:
                l=r
                r+=1
            else:
                maxx = max(maxx, prices[r] - prices[l])
                r+=1

        return maxx