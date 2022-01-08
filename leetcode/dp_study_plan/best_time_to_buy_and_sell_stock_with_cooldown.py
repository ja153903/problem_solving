"""
==================================================
309. Best Time to Buy and Sell Stock with Cooldown
==================================================

=======
Problem
=======

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
    * After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

========
Approach
========

Approach 1:
    This problem might be similar to the other best time problem because we would still want to gain as much profit as we can
    So at any point we have a min_buy we should sell at the next possible day to profit
    This does not work as it doesn't account for strategies that involve holding for more than 1 day

Approach 2:
    We can separate our thought process into 2 states: buy and sell
    b0 and b1 represent buy[i] and buy[i - 1] respectively
    s0, s1, and s2 represent sell[i], sell[i - 1], sell[i - 2]

    These states mean the following:
        buy ~ max profit until index i such that the last transaction is a buy
        sell ~ max profit until index i such that the last transaction is a sell

    Note that here we can optimize for the profit if we have that the last transaction is a sell

    At each price, our buy state makes the following decisions: take a rest or buy at i after selling at some state before i - 1
    Note that we cannot sell at i - 1 then buy at i because of the cooldown rule (which is why we take advantage of sell[i - 2])
        * This translates to buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
    
    Our sell state makes the following decisions: take a rest or sell at i after buying at some previous state before i
        * This translates to sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        b0, b1 = -prices[0], -prices[0]
        s2, s1, s0 = 0, 0, 0

        for i in range(1, len(prices)):
            b0 = max(b1, s2 - prices[i])
            s0 = max(s1, b1 + prices[i])
            b1, s1, s2 = b0, s0, s1

        return s0


    def approach_one(self, prices: List[int]) -> int:
        # This def does not work
        if len(prices) <= 1:
            return 0

        profit = 0
        min_buy = prices[0]
        made_profit = False

        for i in range(1, len(prices)):
            if made_profit:
                made_profit = False
                continue

            min_buy = min(min_buy, prices[i])
            if prices[i] > min_buy:
                profit += prices[i] - min_buy
                made_profit = True

        return profit


if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([1, 2, 3, 0, 2]) == 3
    assert s.maxProfit([1, 2, 0, 9, 2]) == 9
    assert s.maxProfit([1]) == 0
