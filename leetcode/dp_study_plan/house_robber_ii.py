from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.algo(nums[1:]), self.algo(nums[:-1]))

    def algo(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        a, b = nums[0], max(nums[0], nums[1])

        for num in nums[2:]:
            a, b = b, max(a + num, b)

        return b

    def recursive(self, nums: List[int]) -> int:
        return max(
            self.recursive_helper(nums[1:], len(nums) - 2),
            self.recursive_helper(nums[:-1], len(nums) - 2),
        )

    def recursive_helper(self, nums: List[int], n: int) -> int:
        if n < 0:
            return 0

        if n == 0:
            return nums[0]

        if n == 1:
            return max(nums[0], nums[1])

        return max(
            self.recursive_helper(nums, n - 1),
            self.recursive_helper(nums, n - 2) + nums[n],
        )


if __name__ == "__main__":
    s = Solution()

    assert s.recursive([2, 3, 2]) == 3
    assert s.recursive([1, 2, 3, 1]) == 4
    assert s.recursive([1, 2, 3]) == 3

    assert s.rob([2, 3, 2]) == 3
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([1, 2, 3]) == 3
