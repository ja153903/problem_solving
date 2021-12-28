import typing

from data_structures.lists import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: typing.Optional[ListNode], l2: typing.Optional[ListNode]
    ) -> typing.Optional[ListNode]:
        root = ListNode(0)
        runner = root
        carry = 0

        while l1 or l2:
            current = carry

            if l1:
                current += l1.val
                l1 = l1.next

            if l2:
                current += l2.val
                l2 = l2.next

            runner.next = ListNode(current % 10)
            carry = current // 10

            runner = runner.next

        if carry:
            runner.next = ListNode(carry)

        return root.next
