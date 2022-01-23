from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        result = []

        for num, _ in counter.most_common(k):
            result.append(num)

        return result

