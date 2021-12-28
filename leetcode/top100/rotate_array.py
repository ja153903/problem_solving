import typing


class Solution:
    def rotate(self, nums: typing.List[int], k: int) -> None:
        rot = k % len(nums)

        copy = list(nums)

        for i, value in enumerate(nums):
            copy[(i + rot) % len(nums)] = value

        for i, value in enumerate(copy):
            nums[i] = value

