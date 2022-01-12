"""
701. Insert into a Binary Search Tree

=======
Problem
=======

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

========
Approach
========

This problem is just a BST but we have to insert the node. Not sure why this is a Medium problem

"""

from typing import Optional

from data_structures.trees import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        runner = root

        while runner:
            if runner.val < val:
                if not runner.right:
                    runner.right = TreeNode(val=val)
                    break

                runner = runner.right
            else:
                if not runner.left:
                    runner.left = TreeNode(val=val)
                    break

                runner = runner.left

        runner = TreeNode(val=val)

        return root
