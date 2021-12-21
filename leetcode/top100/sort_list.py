from typing import Optional

from data_structures.lists import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # This solution is in O(n lg n) time and O(n) space
        # Optimizations that make sense would be O(lg n) space
        # with merge sort solution (not sure how we would go about
        # doing this with O(1) space since recursion itself would take
        # O(lg n) space)
        values = []

        while head:
            values.append(head.val)
            head = head.next

        values = sorted(values)

        root = ListNode()
        runner = root

        for value in values:
            runner.next = ListNode(val=value)
            runner = runner.next

        return root.next
