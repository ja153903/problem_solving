from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a, b = nums[0], max(nums[0], nums[1])

        for num in nums[2:]:
            a, b = b, max(a + num, b)

        return b

    def recursive(self, nums: List[int]) -> int:
        return self.recursive_helper(nums, len(nums) - 1)

    def recursive_helper(self, nums: List[int], n: int) -> int:
        if n < 0:
            return 0

        if n == 0 or n == 1:
            return max(nums[0], nums[1])

        return max(
            self.recursive_helper(nums, n - 1),
            self.recursive_helper(nums, n - 2) + nums[n],
        )
