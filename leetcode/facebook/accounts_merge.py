# TODO: This question is hard:
# I get it conceptually, but this aint fun
from typing import List, Tuple

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        nodes: List[Tuple[str, str]] = []

        for account, *emails in accounts:
            for email in emails:
                nodes.append((account, email))
        
        return []


if __name__ == "__main__":
    s = Solution()

    s.accountsMerge(
        [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )
