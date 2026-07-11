class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]

        maxi = 0

        for i in prices:
            maxi = max(maxi , i-mini)
            mini = min(mini , i)

        return maxi
        