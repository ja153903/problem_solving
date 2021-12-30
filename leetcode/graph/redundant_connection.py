from typing import List


class UnionFind:
    def __init__(self, nodes: int):
        self.id = [i for i in range(nodes)]
        self.rank = [0] * nodes

    def find(self, i: int) -> int:
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    def union(self, p: int, q: int) -> bool:
        i = self.find(p)
        j = self.find(q)

        if i == j:
            return False

        if self.rank[i] > self.rank[j]:
            self.id[i] = j
        else:
            self.id[j] = i
            if self.rank[i] == self.rank[j]:
                self.rank[i] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()

        for u, v in edges:
            nodes.add(u)
            nodes.add(v)

        uf = UnionFind(len(nodes))

        for u, v in edges:
            # as we go through edges, we end up creating the union
            # between the nodes
            # if at some point we find two nodes that have the same
            # parent, we know that this edge is redundant because
            # they share the same parent node so we can safely remove this
            if not uf.union(u - 1, v - 1):
                return [u, v]

        return []
