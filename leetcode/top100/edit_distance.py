class Solution:
    def brute_force(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        if not word1:
            return len(word2)

        if not word2:
            return len(word1)

        if word1[0] == word2[0]:
            return self.brute_force(word1[1:], word2[1:])

        insert = 1 + self.brute_force(word1, word2[1:])
        delete = 1 + self.brute_force(word1[1:], word2)
        replace = 1 + self.brute_force(word1[1:], word2[1:])

        return min(insert, delete, replace)

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i

        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(
                        table[i - 1][j],        # inserting one
                        table[i][j - 1],        # deleting one
                        table[i - 1][j - 1]     # replacing one
                    )

        return table[-1][-1]
