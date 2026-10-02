class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0


        l = 0
        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                maxProf = max(prices[r] - prices[l], maxProf)
            if prices[r] < prices[l]:
                l = r


        return maxProf