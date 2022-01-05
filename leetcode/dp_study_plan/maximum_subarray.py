from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_, max_so_far = nums[0], nums[0]

        for i in range(1, len(nums)):
            max_so_far = max(max_so_far + nums[i], nums[i])
            max_ = max(max_, max_so_far)

        return max_
