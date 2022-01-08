"""
122. Best Time to Buy and Sell Stock II

=======
Problem
=======

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

========
Approach
========

Approach 1:
    We could modify how we solved the first problem by making sure we buy at the current min_buy, but every time we can get a positive profit, we sell right away.

========
Analysis
========
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]

        for i in range(1, len(prices)):
            min_buy = min(min_buy, prices[i])
            if prices[i] > min_buy:
                profit += prices[i] - min_buy
                min_buy = prices[i]

        return profit


if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
