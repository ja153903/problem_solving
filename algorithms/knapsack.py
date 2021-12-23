"""
0/1 Knapsack Problem

=====
Notes
=====

Given weights and values of n items, put these items in a knapsack of
capacity W to get the maximum total value in the knapsack.

In other words, given two integer arrays val[0...n-1] and wt[0...n-1]
which represent values and weights associated with n items respectively.

Also given an integer W which represents knapsack capacity, find out the
maximum value subset of val[] such that sum of the weights of this subset
is smaller than or equal to W. You cannot break an item, either pick the
complete item or don't pick it (0/1 property).

Note that recursively, this is a top-down approach.
"""
import typing


def knapsack(W: int, wt: typing.List[int], val: typing.List[int], n: int) -> int:
    K = [
        [0 for _ in range(W + 1)]
        for _ in range(n + 1)
    ]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(
                    val[i - 1] + K[i - 1][w - wt[i - 1]],
                    K[i - 1][w]
                )

    return K[n][W]
