from typing import List


"""
======================================================
1567. Maximum Length of Subarray with Positive Product
======================================================

=======
Problem
=======

Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

========
Approach
========

Approach 1:
    Extend solution from Maximum Product Subarray to also keep track of indices
    Can't get this to work because I'm dumb

Approach 2:
    Go through items linearly keeping track of positive product and negative product.
        if num == 0:
            set positive and negative product to 0 since we start over
        else if num > 0:
            increase positive product count
            increase negative product count unless its 0 (if 0, then no need to increase)
        else (if num < 0):
            positive should be 0 if neg == 0 else neg + 1 (since we're swapping)
            negative should be positive + 1 (before swap)

        update max against postive numbers
        
========
Analysis
========

O(n) time and O(1) space
"""


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        result, pos, neg = 0, 0, 0

        for num in nums:
            if num == 0:
                pos, neg = 0, 0
            elif num > 0:
                pos += 1
                neg = 0 if neg == 0 else neg + 1
            else:
                pos, neg = 0 if neg == 0 else neg + 1, pos + 1

            result = max(result, pos)

        return result

    def modified_max_product_subarray(self, nums: List[int]) -> int:
        # This one doesn't work
        max_so_far, min_so_far = nums[0], nums[0]
        max_index_so_far = [0, 0]
        min_index_so_far = [0, 0]

        for i in range(1, len(nums)):
            if max_so_far * nums[i] < min_so_far or min_so_far * nums[i] < min_so_far:
                min_index_so_far[1] = i
            else:
                min_index_so_far = [i, i]

            if max_so_far * nums[i] > max_so_far or min_so_far * nums[i] > max_so_far:
                max_index_so_far[1] = i
            else:
                max_index_so_far = [i, i]

            min_so_far, max_so_far = min(
                max_so_far * nums[i], min_so_far * nums[i], nums[i]
            ), max(max_so_far * nums[i], min_so_far * nums[i], nums[i])

        print(max_index_so_far)
        print(min_index_so_far)

        return max(
            max_index_so_far[1] - max_index_so_far[0] + 1,
            min_index_so_far[1] - min_index_so_far[0] + 1,
        )


if __name__ == "__main__":
    s = Solution()

    assert s.getMaxLen([1, -2, -3, 4]) == 4
