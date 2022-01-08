"""
=========================================================
714. Best Time to Buy and Sell Stock with Transaction Fee
=========================================================

=======
Problem
=======

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

========
Approach
========

Up to the ith day, what is the max profit we can make?
* On the ith day, we have two states to land on: buy and sell

So we have two types of state to look at: max profit at ith day when transaction is a buy and max profit at ith day when transaction is a sell

buy[0] = -prices[0]
sell[0] = 0 # you cannot sell on the first day

buy[1] = - prices[0] ~ same state as buy[0] because there's no way to have sold anything at sell[0]

sell[1] = max(sell[0], buy[0] + prices[i] - fee)

Now for the third value, the max profit is either what we had at buy[1] or sell[i - 1] - prices[i]
buy[2] = max(buy[1], sell[i - 1] - prices[i])
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0

        buy = [0] * len(prices)
        sell = [0] * len(prices)

        buy[0], buy[1] = -prices[0], -prices[0]

        for i in range(1, len(prices)):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])

        return sell[-1]
