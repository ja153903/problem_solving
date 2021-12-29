import typing
import collections


class Solution:
    def findCenter(self, edges: typing.List[typing.List[int]]) -> int:
        """
        There is an undirected star graph consisting of n nodes labeled from 1 to n.
        A star graph is a graph where there is one center node and exactly n - 1
        edges that connect the center node with every other node.
        """
        graph = collections.defaultdict(set)
        num_nodes = 0
        visited = set()

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

            if u not in visited:
                num_nodes += 1
                visited.add(u)

            if v not in visited:
                num_nodes += 1
                visited.add(v)

        for key, children in graph.items():
            if len(children) == num_nodes - 1:
                return key

        return -1


if __name__ == "__main__":
    s = Solution()

    edges = [[1, 2], [2, 3], [4, 2]]
    assert s.findCenter(edges) == 2

    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    assert s.findCenter(edges) == 1
