class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

    def linear_space(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
