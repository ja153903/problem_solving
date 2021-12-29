import typing


# Remember this template for UnionFind problems
class UnionFind:
    def __init__(self, nodes: int):
        self.id = [i for i in range(nodes)]
        self.rank = [0] * nodes
        self.count = nodes

    def find(self, i: int) -> int:
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    def union(self, p: int, q: int) -> None:
        i = self.find(p)
        j = self.find(q)

        if i == j:
            return

        if self.rank[i] > self.rank[j]:
            self.id[i] = j
        else:
            self.id[j] = i
            if self.rank[i] == self.rank[j]:
                self.rank[i] += 1

        self.count -= 1


class Solution:
    def findCircleNum(self, isConnected: typing.List[typing.List[int]]) -> int:
        # the idea here is to use the union find algorithm
        # so that we can tell how many disjoint sets there are
        num_nodes = len(isConnected)

        uf = UnionFind(num_nodes)

        for i in range(num_nodes - 1):
            for j in range(i + 1, num_nodes):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.count


if __name__ == "__main__":
    s = Solution()

    assert (
        s.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1
    )
