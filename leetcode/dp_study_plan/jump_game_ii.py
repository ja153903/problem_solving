from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n, step, start, end = len(nums), 0, 0, 0

        while end < n - 1:
            step += 1

            max_end = end + 1

            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step

                max_end = max(max_end, i + nums[i])

            start, end = end + 1, max_end

        return step


if __name__ == "__main__":
    s = Solution()

    assert s.jump([2, 3, 1, 1, 4]) == 2
