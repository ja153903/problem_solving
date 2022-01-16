"""
1570. Dot Product of Two Sparse Vector

=== Approach ===

The idea with my solution here is that we keep track of the indices of nonzero values.

"""
from typing import List, Dict


class SparseVector:
    def __init__(self, nums: List[int]):
        self.mp: Dict[int, int] = {i: num for i, num in enumerate(nums) if num != 0}
    
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0

        for key, value in self.mp.items():
            result += value * vec.mp.get(key, 0)

        return result
