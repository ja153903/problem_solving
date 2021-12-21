class Solution:
    def solve(self, nums, k):
        seen = set()

        for num in nums:
            if k - num in seen:
                return True

            seen.add(num)

        return False
