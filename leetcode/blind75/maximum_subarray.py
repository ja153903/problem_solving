"""
====================
53. Maximum Subarray
====================

=======
Problem
=======

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

========
Approach
========

This problem at this point has become a trivia problem.

It screams "Hey, do you know Kadane's algorithms?"

The idea behind Kadane's algorithm is that to find the maximum subarray sum
is to either continue adding to the max you've collected so far or start over
at the most recent element you've encountered.

This solution runs in O(n) time and O(1) space.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_, max_so_far = nums[0], nums[0]

        for i in range(1, len(nums)):
            max_so_far = max(max_so_far + nums[i], nums[i])
            max_ = max(max_, max_so_far)

        return max_
