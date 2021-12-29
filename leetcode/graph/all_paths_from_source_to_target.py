import typing


class Solution:
    def allPathsSourceTarget(
        self, graph: typing.List[typing.List[int]]
    ) -> typing.List[typing.List[int]]:
        # find all paths from 0 to n - 1 where n = len(graph)
        def dfs(node: int, result: typing.List[int], current: typing.List[int], visited: typing.Set[int]):
            if node == len(graph) - 1:
                # this means we're at the end
                result.append(list(current))
                return
            else:
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        dfs(child, result, current + [child], visited)
                        visited.remove(child)

        result = []

        dfs(0, result, [0], set([0]))

        return result


if __name__ == "__main__":
    s = Solution()

    graph = [[1, 2], [3], [3], []]
    result = s.allPathsSourceTarget(graph)
    expected = [[0, 1, 3], [0, 2, 3]]

    print(result)

    assert result == expected
