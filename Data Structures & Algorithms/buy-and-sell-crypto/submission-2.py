class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        maxi = 0
        mini = prices[0]
        for n in prices:
            maxi = max(maxi , n - mini)
            mini = min(mini , n)

        return maxi
        