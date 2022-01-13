"""
42. Trapping Rain Water

=======
Problem
=======

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

========
Approach
========

The idea with this problem is to keep track of the max_left and max_right values, but every time we should check if we can keep adding
to the amount of water that we're trapping i.e. every time the current left or right value is less than the max, this means we can trap water
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        i, j = 0, len(height) - 1
        max_left, max_right = height[i], height[j]

        while i < j:
            if height[i] < height[j]:
                if height[i] > max_left:
                    max_left = height[i]
                else:
                    result += max_left - height[i]

                i += 1
            else:
                if height[j] > max_right:
                    max_right = height[j]
                else:
                    result += max_right - height[j]
                j -= 1

        return result


if __name__ == "__main__":
    s = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert s.trap(height) == 6
