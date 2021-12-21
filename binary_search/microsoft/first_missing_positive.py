from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        if not nums:
            return 1

        min_num = nums[0]
        max_num = nums[0]

        for i in range(1, len(nums)):
            min_num = min(min_num, nums[i])
            max_num = max(max_num, nums[i])

        as_set = set(nums)

        for i in range(1, max_num + 1):
            if i not in as_set and i > 0:
                return i

        return max(max_num + 1, 1)
