from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # this problem requires a modification of Kadane's algorithm
        # TODO: Figure out why we need to do this by reading the discussion board again:
        total, max_sum, cur_max, min_sum, cur_min = 0, nums[0], 0, nums[0], 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
            total += num

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
