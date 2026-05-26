from typing import List
from collections import Counter

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            # print(i, buy_price,"--")
            current_price = prices[i]
            if current_price < buy_price:
                buy_price = current_price
            if current_price > buy_price:
                profit = max(profit, current_price - buy_price)
        # print(buy_price,)
        return profit


sol = Solution()
print(sol.maxProfit([7, 6, 4, 3, 1]))
