"""
452. Minimum Number of Arrows to Burst Balloons

=======
Problem
=======

There are some spherical balloons taped onto a flat wall that represents the XY-plane.
The balloons are represented as a 2D integer array points where points[i] = [x_start, x_end]
denotes a balloon whose horizontal diameter stretches between x_start and x_end. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
A balloon with x_start and x_end is burst by an arrow shot at x if x_start <= x <= x_end. 
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Examples:
    points = [[10,16],[2,8],[1,6],[7,12]]

    Can we merge these intervals?

    [[1, 8], [7, 16]] => 2 arrows needed

    points = [[1,2],[2,3],[3,4],[4,5]]
    

========
Approach
========

We sort the intervals here by the end value.
Once we have that sorted, we keep track of the minimum end.
As long as the start value is less than or equal to the minimum end,
we can keep merging them into the same interval. Otherwise, we have to
increase the count and set the new minimum end.
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda p: p[1])

        result, end = 0, -float('inf')

        for point in points:
            if point[0] > end:
                result += 1
                end = point[1]

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert s.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert s.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
