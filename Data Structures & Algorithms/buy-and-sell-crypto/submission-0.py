class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxProfit = 0

        for i in prices:
            if i < min:
                min = i
            j = i - min
            if j > maxProfit:
                maxProfit = j
        return maxProfit