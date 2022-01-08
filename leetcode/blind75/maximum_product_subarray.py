"""
152. Maximum Product Subarray

=======
Problem
=======

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

========
Approach
========

This problem can be approached with Kadane's algorithm. However, we want to make sure
that we take care of the minimum value because if we come across a negative value we
can multiply that minimum value with the current minimum result so potentially get a maximum value
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far, min_so_far, max_ = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            min_so_far, max_so_far = min(
                max_so_far * nums[i], min_so_far * nums[i], nums[i]
            ), max(max_so_far * nums[i], min_so_far * nums[i], nums[i])
            max_ = max(max_, max_so_far)

        return max_

