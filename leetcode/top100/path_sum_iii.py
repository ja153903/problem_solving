from typing import Optional

from data_structures.trees import TreeNode


class Solution:
    def __init__(self):
        self.num_paths = 0

    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        self.dfs(root, target_sum)

        return self.num_paths

    def dfs(self, root: Optional[TreeNode], target_sum: int) -> None:
        if not root:
            return

        self.go_into_path(root, target_sum)
        self.dfs(root.left, target_sum)
        self.dfs(root.right, target_sum)

    def go_into_path(self, root: Optional[TreeNode], target_sum: int) -> None:
        if not root:
            return

        if root.val == target_sum:
            self.num_paths += 1

        self.go_into_path(root.left, target_sum - root.val)
        self.go_into_path(root.right, target_sum - root.val)