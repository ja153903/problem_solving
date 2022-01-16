from data_structures.trees import TreeNode

from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        mp = defaultdict(list)
        queue = deque()

        level = 0
        queue.append((root, level))

        while queue:
            front, lvl = queue.popleft()

            mp[lvl].append(front.val)

            if front.left:
                queue.append((front.left, lvl - 1))

            if front.right:
                queue.append((front.right, lvl + 1))

        result = sorted([(key, value) for key, value in mp.items()], key=lambda t: t[0])

        return [value for _, value in result]
