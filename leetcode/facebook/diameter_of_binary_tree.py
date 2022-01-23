from data_structures.trees import TreeNode

from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            self.max = max(self.max, left + right)

            return max(left, right) + 1

        depth(root)

        return self.max
