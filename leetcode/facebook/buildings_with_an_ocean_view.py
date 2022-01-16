from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        local_max = heights[-1]

        result.append(len(heights) - 1)

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > local_max:
                result.append(i)
                local_max = heights[i]

        return result[::-1]

