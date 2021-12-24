import typing

from data_structures.lists import ListNode


class Solution:
    def isPalindrome(self, head: typing.Optional[ListNode]) -> bool:
        result = []

        while head:
            result.append(head.val)
            head = head.next

        return result == result[::-1]
