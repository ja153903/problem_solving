"""
==========
1. Two Sum
==========

=======
Problem
=======

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

========
Approach
========

To solve this question with a linear scan, what we can do is store the seen values and check to see
if we have target - value as a key within the dictionary
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            if target - val in seen:
                return [seen[target - val], i]

            seen[val] = i

        return []
