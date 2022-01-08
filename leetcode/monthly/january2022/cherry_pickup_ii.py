"""
======================
1463. Cherry Pickup II
======================

=======
Problem
=======

You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

* Robot #1 is located at the top-left corner (0, 0), and
* Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of cherries collection using both robots by following the rules below:

* From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
* When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
* When both robots stay in the same cell, only one takes the cherries.
* Both robots cannot move outside of the grid at any moment.
* Both robots should reach the bottom row in grid.

========
Approach
========

Each robot can walk on either diagonal or straight down

We can utilize the lru_cache in Python to help use solve this.

The idea is to do a DFS at each step.

First we collect the cherries we can collect at our current step
Then we do a DFS for each possible combination of steps and find the maximum
path from that.

We then return that answer + the number of cherries we've taken at this step

the lru_cache allows us to not have to define the typical DP solution since
it'll work exactly the same way

========
Analysis
========

This solution works in O(9 * m * n^2) time complexity where m is the number of rows and n is the number of columns
Space complexity is O(m * n^2)
"""

from typing import List
from functools import lru_cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(r, c1, c2):
            if r == m:
                return 0

            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
            ans = 0

            for nc1 in range(c1 - 1, c1 + 2):
                for nc2 in range(c2 - 1, c2 + 2):
                    if 0 <= nc1 < n and 0 <= nc2 < n:
                        ans = max(ans, dfs(r + 1, nc1, nc2))

            return ans + cherries

        return dfs(0, 0, n - 1)
