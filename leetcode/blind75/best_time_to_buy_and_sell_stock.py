"""
====================================
121. Best Time to Buy and Sell Stock
====================================

=======
Problem
=======

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

========
Approach
========

Given that we want to capture the largest profit we can find, we need to find a global minimum and some relative maximum such that
the index of the global minimum, i, is less than the index of the global maximum j

To do this in a linear scan, we can continuously update the minimum index we can buy at as well as computing the maximum profit each time
we can sell for a profit.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_buy = prices[0]
        profit = 0

        for price in prices:
            minimum_buy = min(minimum_buy, price)
            profit = max(profit, price - minimum_buy)

        return minimum_buy
