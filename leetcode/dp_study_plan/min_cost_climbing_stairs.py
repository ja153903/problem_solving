from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    # Top Down DP
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(index: int, dp: List[int]) -> int:
            if index < 0:
                return 0

            if index in [0, 1]:
                return cost[index]

            if dp[index] != 0:
                return dp[index]

            dp[index] = cost[index] + min(helper(index - 1, dp), helper(index - 2, dp))

            return dp[index]

        n = len(cost)
        dp = [0] * n

        return min(helper(n - 1, dp), helper(n - 2, dp))
    
    def bottom_up_dp(self, costs: List[int]) -> int:
        n = len(costs)
        dp = [0] * n

        for i, val in enumerate(costs):
            if i < 2:
                dp[i] = val
            else:
                dp[i] = val + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])


    def recursive(self, costs: List[int]) -> int:
        def helper(index: int, cost: int) -> int:
            if index < 0:
                return cost

            if (index, cost) in self.cache:
                return self.cache[(index, cost)]

            result = min(helper(index - 1, cost), helper(index - 2, cost)) + costs[index]

            self.cache[(index, cost)] = result

            return result

        n = len(costs)

        self.cache = {}

        result = min(
            helper(n - 1, 0),
            helper(n - 2, 0),
        )

        return result


if __name__ == "__main__":
    s = Solution()

    cost = [10, 15, 20]
    assert s.recursive(cost) == 15
    assert s.minCostClimbingStairs(cost) == 15
    assert s.bottom_up_dp(cost) == 15

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert s.recursive(cost) == 6
    assert s.minCostClimbingStairs(cost) == 6
    assert s.bottom_up_dp(cost) == 6
