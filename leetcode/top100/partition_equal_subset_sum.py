import typing


class Solution:
    def canPartition(self, nums: typing.List[int]) -> bool:
        _sum = sum(nums)

        if _sum & 1 == 1:
            return False

        _sum //= 2

        dp = [False for _ in range(_sum + 1)]
        dp[0] = True

        for num in nums:
            for i in range(_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[_sum]

    def recursive(self, nums: typing.List[int]) -> bool:
        def helper(left: int, right: int, i: int) -> bool:
            if i == len(nums):
                return left == right

            return (
                helper(left + nums[i], right, i + 1) or
                helper(left, right + nums[i], i + 1)
            )

        if not nums:
            return True

        return helper(0, 0, 0)


if __name__ == '__main__':
    s = Solution()

    assert s.recursive([1, 5, 11, 5])
    assert not s.recursive([1, 2, 3, 5])
