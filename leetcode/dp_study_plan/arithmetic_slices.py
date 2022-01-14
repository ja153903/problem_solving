"""
413. Arithmetic Slices

=======
Problem
=======

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

========
Approach
========

We know that the array has to have a length of at least 3. This is our base case

The brute force approach here is to check if any subsequence with length of at least 3 is a sequence
"""

from typing import List


class Solution:
    def is_sequence(self, nums: List[int], start: int, end: int) -> bool:
        diff = None

        for i in range(start + 1, end + 1):
            current_diff = nums[i] - nums[i - 1]

            if diff is None:
                diff = current_diff
            elif diff != current_diff:
                return False

        return True
    
    def brute_force(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        result = 0

        for i in range(len(nums) - 2):
            for j in range(i + 2, len(nums)):
                if self.is_sequence(nums, i, j):
                    result += 1

        return result


    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        curr, sm = 0, 0

        for i in range(2, len(nums)):
            # we should just check the diff of the last 3
            # if currently a sequence, we update curr
            # then once we update curr, we add that new one to the sum
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr += 1
                sm += curr
            else:
                curr = 0

        return sm


if __name__ == "__main__":
    s = Solution()

    assert s.brute_force([1, 2, 3, 4]) == 3
    assert s.brute_force([1]) == 0

    assert s.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert s.numberOfArithmeticSlices([1]) == 0
