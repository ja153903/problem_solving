import collections
from typing import List


class Solution:
    def brute_force(self, matrix: List[List[int]], target: int) -> bool:
        queue = collections.deque()
        visited = set()
        queue.append((0, 0))

        directions = [(1, 0), (0, 1)]

        while queue:
            x, y = queue.popleft()
            visited.add((0, 0))

            if matrix[x][y] == target:
                return True

            for dx, dy in directions:
                cx, cy = x + dx, y + dy

                if cx < 0 or cy < 0 or cx >= len(matrix) or cy >= len(matrix[0]) or (cx, cy) in visited or matrix[cx][cy] > target:
                    continue

                queue.append((cx, cy))

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        i, j = 0, len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False


if __name__ == '__main__':
    s = Solution()
    assert s.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
    assert not s.searchMatrix(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)
