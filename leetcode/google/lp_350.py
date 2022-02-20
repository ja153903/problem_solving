from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)

        result = []

        for key, value in n1.items():
            if key in n2:
                for _ in range(min(value, n2[key])):
                    result.append(key)

        return result

