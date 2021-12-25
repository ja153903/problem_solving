import typing


class Solution:
    def searchInsert(self, nums: typing.List[int], target: int) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    s = Solution()

    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3], 2) == 1
    assert s.searchInsert([1], 1) == 0
