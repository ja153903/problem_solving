from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0

    # This solution will still timeout
    def canJump_tle(self, nums: List[int]) -> bool:
        self.memo = {}

        return self.recursive(nums, 0)

    def recursive(self, nums: List[int], n: int) -> bool:
        if n in self.memo:
            return self.memo[n]

        if n >= len(nums) - 1:
            return True

        result = False

        for i in range(1, nums[n] + 1):
            if n + i not in self.memo:
                self.memo[n + i] = self.recursive(nums, n + i)

            result = result or self.memo[n + i]

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.canJump([2, 3, 1, 1, 4])
    assert not s.canJump([3, 2, 1, 0, 4])
    assert not s.canJump([0, 2, 3])
    assert not s.canJump([1, 0, 1, 0])
