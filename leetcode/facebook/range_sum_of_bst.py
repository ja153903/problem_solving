from data_structures.trees import TreeNode

from typing import Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        ts = 0

        if low <= root.val <= high:
            ts += root.val

        if low < root.val:
            ts += self.rangeSumBST(root.left, low, high)

        if high > root.val:
            ts += self.rangeSumBST(root.right, low, high)

        return ts

