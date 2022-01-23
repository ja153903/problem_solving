from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = defaultdict()
        graph = defaultdict(set)

        for account, *emails in accounts:
            for email in emails:
                graph[email].add(emails[0])
                graph[emails[0]].add(email)
                names[email] = account

        comps, seen, i = defaultdict(list), set(), 0

        def dfs(node, i):
            comps[i].append(node)
            seen.add(node)
            for neib in graph[node]:
                if neib not in seen:
                    dfs(neib, i)

        for email in graph:
            if email not in seen:
                dfs(email, i)
                i += 1

        return [[names[val[0]]] + sorted(val) for _, val in comps.items()]


if __name__ == "__main__":
    s = Solution()

    print(
        s.accountsMerge(
            [
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ]
        )
    )
