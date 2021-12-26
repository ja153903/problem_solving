import typing

from data_structures.lists import ListNode


class Solution:
    def detectCycle(self, head: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        if not head:
            return None

        visited = set()

        while head:
            if head in visited:
                return head

            visited.add(head)

            head = head.next

        return None

    def using_two_pointer(self, head: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast, entry = head, head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next

                return entry

        return None