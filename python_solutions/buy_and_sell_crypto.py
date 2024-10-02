class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            diff = max(diff, p - lowest)
        return diff