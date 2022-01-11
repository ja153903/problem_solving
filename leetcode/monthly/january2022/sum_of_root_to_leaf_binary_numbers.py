"""
========================================
1022. Sum of Root To Leaf Binary Numbers
========================================

=======
Problem
=======

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

========
Approach
========

Approach 1:
    Generate all possible binary numbers and convert each one into an integer
    Then return the sum of the list

    This is done by doing a DFS where each time we hit the leaf, we add the resulting string into some array.
    This array is then mapped over to convert each binary string into an integer.
    Then we find the sum of every element in the list.

    Note that a leaf is a node with no left and right children
"""

from typing import Optional, List

from data_structures.trees import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = []

        self.dfs(root, result, [])

        return sum([int(bin, 2) for bin in result])

    def dfs(self, node: Optional[TreeNode], result: List[str], current: List[str]) -> None:
        if not node:
            return

        to_add = str(node.val)

        if not node.left and not node.right:
            # this means that there are no children
            result.append(''.join(current + [to_add]))
            return

        if node.left:
            self.dfs(node.left, result, current + [to_add])

        if node.right:
            self.dfs(node.right, result, current + [to_add])
