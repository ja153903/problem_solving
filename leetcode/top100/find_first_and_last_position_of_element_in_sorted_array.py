import typing


class Solution:
    def searchRange(self, nums: typing.List[int], target: int) -> typing.List[int]:
        result = [-1, -1]

        if not nums:
            return result

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target:
            return result

        result = [left, left]

        right = len(nums) - 1

        while left < right:
            # this helps us bias mid
            mid = (left + right) // 2 + 1

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        result[1] = right

        return result


if __name__ == "__main__":
    s = Solution()

    result = s.searchRange([5, 7, 7, 8, 8, 10], 8)
    assert result == [3, 4]

    result = s.searchRange([5, 7, 7, 8, 8, 10], 6)
    assert result == [-1, -1]

    result = s.searchRange([5, 7, 7, 8, 8, 10], 0)
    assert result == [-1, -1]

    result = s.searchRange([5, 7, 7, 8, 8, 10], 7)
    assert result == [1, 2]

    result = s.searchRange([2, 2], 2)
    assert result == [0, 1]
