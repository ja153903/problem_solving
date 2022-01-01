class Solution:
    """
    With a number of dynamic programming questions, we have to make sure that
    we optimize the recursive solution by caching or memoizing results
    from already computed subproblems
    """
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        a, b = 0, 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

    def linear_fib(self, n: int) -> int:
        # Solution with O(n) space used
        if n == 0:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def recursive(self, n: int) -> int:
        if n <= 1:
            return 1

        return self.recursive(n - 1) + self.recursive(n - 2)

