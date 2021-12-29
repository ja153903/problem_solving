import typing


class Solution:
    def findSmallestSetOfVertices(
        self, n: int, edges: typing.List[typing.List[int]]
    ) -> typing.List[int]:
        """
        Given a DAG with n vertices and an array of edges,
        find the smallest set of vertices from which all nodes
        in the graph are reachable.

        Note that given that this is a DAG, we know that if a
        node has no incoming edges, then those are nodes
        from which we start the path.

        So we just need to enumerate the nodes that have
        no incoming edges.
        """
        incoming = [0] * n

        for _, to in edges:
            incoming[to] += 1

        return [i for i, value in enumerate(incoming) if value == 0]
