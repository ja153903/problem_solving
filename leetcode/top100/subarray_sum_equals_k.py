import collections
import typing


class Solution:
    def brute_force(self, nums: typing.List[int], k: int) -> int:
        result = 0

        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                if current == k:
                    result += 1

        return result

    def subarraySum(self, nums: typing.List[int], k: int) -> int:
        _sum, result = 0, 0

        presum = collections.defaultdict(int)
        presum[0] = 1

        for i, num in enumerate(nums):
            # continuously add values
            _sum += num

            # if the total sum - k is in the map
            if _sum - k in presum:
                # we add that to the result
                result += presum[_sum - k]

            presum[_sum] = presum.get(_sum, 0) + 1

        return result
