import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected_graph = collections.defaultdict(set)
        edges_as_str = set([f"{fr},{to}" for fr, to in connections])
        
        for fr, to in connections:
            undirected_graph[fr].add(to)
            undirected_graph[to].add(fr)

        count = 0

        queue = collections.deque()
        visited = set()

        queue.append(0)
        visited.add(0)

        while queue:
            front = queue.popleft()

            for child in undirected_graph.get(front, []):
                if child not in visited:
                    visited.add(child)

                    if f"{child},{front}" not in edges_as_str:
                        count += 1

                    queue.append(child)

        return count


if __name__ == "__main__":
    s = Solution()

    assert s.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3
