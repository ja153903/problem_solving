import typing


class Solution:
    def regionsBySlashes(self, grid: typing.List[int]) -> int:
        """
        This problem is solved by making the image 3d rather than 2d
        because this gives us a better picture of where the areas are

        This problem then becomes the number of islands problem
        """
        n = len(grid)
        upscaled = [[0 for _ in range(3 * n)] for _ in range(3 * n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    upscaled[3 * i][3 * j + 2] = 1
                    upscaled[3 * i + 1][3 * j + 1] = 1
                    upscaled[3 * i + 2][3 * j] = 1
                elif grid[i][j] == "\\":
                    upscaled[3 * i][3 * j] = 1
                    upscaled[3 * i + 1][3 * j + 1] = 1
                    upscaled[3 * i + 2][3 * j + 2] = 1

        islands = 0

        for i in range(3 * n):
            for j in range(3 * n):
                if upscaled[i][j] == 0:
                    if self.dfs(upscaled, i, j) > 0:
                        islands += 1

        return islands

    def dfs(self, upscaled: typing.List[typing.List[int]], i: int, j: int) -> int:
        if (
            i < 0
            or j < 0
            or i >= len(upscaled)
            or j >= len(upscaled)
            or upscaled[i][j] != 0
        ):
            return 0

        upscaled[i][j] = 2

        return (
            1
            + self.dfs(upscaled, i + 1, j)
            + self.dfs(upscaled, i - 1, j)
            + self.dfs(upscaled, i, j + 1)
            + self.dfs(upscaled, i, j - 1)
        )


if __name__ == "__main__":
    s = Solution()

    assert s.regionsBySlashes([" /", "/ "]) == 2
    assert s.regionsBySlashes(["/\\", "\\/"]) == 5
