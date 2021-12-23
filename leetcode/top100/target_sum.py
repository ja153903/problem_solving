import typing


class Solution:
    def tle(self, nums: typing.List[int], target: int) -> int:
        result = []

        self.backtrack_tle(nums, target, 0, result, 0)

        return sum(result)

    def backtrack_tle(self, nums: typing.List[int], target: int, current: int, result: typing.List[int], index: int):
        # need to cache results of this one
        # key should be index and the current sum
        if index == len(nums):
            if current == target:
                result.append(1)
        else:
            self.backtrack_tle(nums, target, current + nums[index], result, index + 1)
            self.backtrack_tle(nums, target, current - nums[index], result, index + 1)

    # This problem is an application of the 0/1 Knapsack problem
    def findTargetSumWays(self, nums: typing.List[int], target: int) -> int:
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, target, index, curr_sum)

    def dp(self, nums: typing.List[int], target: int, index: int, curr_sum: int) -> int:
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        if index < 0 and curr_sum == target:
            return 1

        if index < 0:
            return 0

        positive = self.dp(nums, target, index - 1, curr_sum + nums[index])
        negative = self.dp(nums, target, index - 1, curr_sum - nums[index])

        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]


if __name__ == '__main__':
    s = Solution()

    result = s.findTargetSumWays([1, 1, 1, 1, 1], 3)
    assert result == 5

    result = s.findTargetSumWays([1], 1)
    assert result == 1
