from typing import List

"""
===========================
1014. Best Sightseeing Pair
===========================

=======
Problem
=======

You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

========
Approach
========

Approach 1:
    Note that the optimal way to get the best sightseeing spot is to look at pairwise items
    This is because we see that i - j < 0 for all iterations. So what we want to do
    is just minimize how much we're getting penalized by the time decay and pairwise transactions are the way to go
    In this case, we initialize our max_i to be the first value - 1
    On each iteration, we add value + max_i and see if we need to update the result
    Then max_i is updated to the max between max_i and value. max_i is then decremented by 1

"""


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result, current = 0, 0

        for value in values:
            result = max(result, current + value)
            current = max(current, value) - 1

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
