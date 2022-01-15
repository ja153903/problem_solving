"""
=======================
217. Contains Duplicate
=======================

=======
Problem
=======

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

========
Approach
========

Approach 1:
    This problem can easily be solved by using a set. We can linearly scan each number and if there exists some number during our scan that
    is in the set, then we return true

    This solution takes O(n) time and space
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
