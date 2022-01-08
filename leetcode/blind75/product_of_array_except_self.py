"""
=================================
238. Product of Array Except Self
=================================

=======
Problem
=======

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

========
Approach
========

Approach 1:
    This problem should run in O(n) time without the use of division.
    One approach we can use to solve this problem is to linearly scan twice.

    The first scan should be going from left to right where at each point, we multiply
    the result by the previous number and never itself:
        [1, 2, 3, 4] => [1, 1, 2, 6]

    The second scan should go from right to left where at each point, we multiply by
    the values from the right side excluding itself. So this means that we should have
    something like this:
        [1, 1, 2, 6] => [24, 12, 8, 6]

    How does this happen on the second scan? We should keep track of a multiplier that increases
    by the value that we don't apply to that index i.e. itself

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        right = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
