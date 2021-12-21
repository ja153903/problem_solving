from typing import Optional

from data_structures.trees import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return helper(left.left, right.right) and helper(left.right, right.left)

        if not root:
            return True

        return helper(root.left, root.right)
