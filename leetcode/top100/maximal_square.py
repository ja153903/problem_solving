import typing


class Solution:
    def maximalSquare(self, matrix: typing.List[typing.List[str]]) -> int:
        grid = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        max_side = 0

        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == "1":
                    grid[i][j] = 1 + min(
                        grid[i][j - 1],
                        grid[i - 1][j],
                        grid[i - 1][j - 1]
                    )
                    max_side = max(max_side, grid[i][j])

        return max_side * max_side