from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for price in prices[1:]:
            if price<buy:
                buy = price
            elif price-buy> maxProfit:
                maxProfit = price-buy
        return maxProfit