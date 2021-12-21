import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0:
            return 0

        count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            count += 1
            size = len(queue)

            for i in range(size):
                front = queue.popleft()
                for dx, dy in directions:
                    x = front[0] + dx
                    y = front[1] + dy

                    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0 or grid[x][y] == 2:
                        continue

                    grid[x][y] = 2

                    queue.append((x, y))

                    fresh -= 1

        return count - 1 if fresh == 0 else -1
