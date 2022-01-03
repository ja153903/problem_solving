from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * (n + 1)
        outgoing = [0] * (n + 1)

        for u, v in trust:
            incoming[v] += 1
            outgoing[u] += 1

        for i in range(1, n + 1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i

        return -1
