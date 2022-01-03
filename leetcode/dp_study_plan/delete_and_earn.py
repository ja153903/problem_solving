from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        This problem can be reduced to house robbers

        The reason is that, we don't care about the order
        the numbers are presented with. We just know that
        we can't pick adjacent pairs. Since we're also
        trying to maximize the number of points, the problem
        then becomes framed similarly.
        """
        counter = Counter(nums)
        points = [counter.get(i, 0) * i for i in range(0, 10 ** 4 + 1)]

        a, b = points[0], max(points[0], points[1])

        for i in range(2, 10 ** 4 + 1):
            a, b = b, max(a + points[i], b)

        return b


if __name__ == "__main__":
    s = Solution()

    assert s.deleteAndEarn([3, 4, 2]) == 6
    assert s.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
