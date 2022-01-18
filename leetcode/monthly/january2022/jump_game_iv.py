"""
1345. Jump Game IV

=======
Problem
=======

Given an array of integers arr, you are initially positioned at the first index of the array

In one step, you can jump from index i to index:
    * i + 1 where i + 1 < arr.length
    * i - 1 where i - 1 >= 0
    * j where arr[i] == arr[j] and i != j

Return the minimum number of steps to reach the last index of the array

Notice that you cannot jump outside of the array at any time

========
Approach
========
"""

from typing import List


class Solution:
    def minJump(self, arr: List[int]) -> int:
        pass