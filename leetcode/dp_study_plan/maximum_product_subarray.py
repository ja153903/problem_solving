from typing import List

"""
=============================
152. Maximum Product Subarray
=============================

=======
Problem
=======

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

========
Approach
========

Brute Force:
    The brute force approach here is to go through all potential contiguous subarrays
    This will take O(n^2) time and O(1) space

Approach 1:
    Let's try using Kadane's algorithm and see if we can come up with counter-examples
    This does not work for arrays with all negative integers

Approach 2:
    Modify Kadane by also taking into consideration the minimum so far
    This is because if we have a negative number, we can multiply the minimum by that negative number
    to potentially get a maximum

========
Analysis
========

Modified Kadane takes O(n) time and O(1) space
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far, min_so_far, max_ = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            min_so_far, max_so_far = min(
                max_so_far * nums[i], min_so_far * nums[i], nums[i]
            ), max(max_so_far * nums[i], min_so_far * nums[i], nums[i])
            max_ = max(max_, max_so_far)

        return max_

    def kadane(self, nums: List[int]) -> int:
        # This solution doesn't work for all negative items
        max_so_far, max_ = nums[0], nums[0]

        for i in range(1, len(nums)):
            max_so_far = max(max_so_far * nums[i], nums[i])
            max_ = max(max_, max_so_far)

        return max_

    def modified_kadane(self, nums: List[int]) -> int:
        max_so_far, min_so_far, max_ = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            min_so_far, max_so_far = min(
                max_so_far * nums[i], min_so_far * nums[i], nums[i]
            ), max(max_so_far * nums[i], min_so_far * nums[i], nums[i])
            max_ = max(max_, max_so_far)

        return max_


if __name__ == "__main__":
    s = Solution()

    # assert s.maxProduct([2, 3, -2, 4]) == 6
    # assert s.maxProduct([-2, 0, -1]) == 0

    # assert s.kadane([2, 3, -2, 4]) == 6
    # assert s.kadane([-2, 0, -1]) == 0
    # assert s.kadane([-2, -3, -4]) == 12
    # assert s.kadane([-2, -3, -2, -4]) == 48

    assert s.modified_kadane([2, 3, -2, 4]) == 6
    assert s.modified_kadane([-2, 0, -1]) == 0
    assert s.modified_kadane([-2, -3, -4]) == 12
    assert s.modified_kadane([-2, -3, -2, -4]) == 48
