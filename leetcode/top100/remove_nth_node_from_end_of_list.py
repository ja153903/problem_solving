import typing

from data_structures.lists import ListNode


class Solution:
    def removeNthFromEnd(
        self, head: typing.Optional[ListNode], k: int
    ) -> typing.Optional[ListNode]:
        nodes = []

        while head:
            nodes.append(head.val)
            head = head.next

        # nth from the end is just the n - kth index
        root = ListNode()
        runner = root
        n = len(nodes)

        for i, value in enumerate(nodes):
            if i != n - k:
                runner.next = ListNode(value)
                runner = runner.next

        return root.next

