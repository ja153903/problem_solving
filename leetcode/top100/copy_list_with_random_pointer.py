import typing

from data_structures.lists import Node


class Solution:
    def copyRandomList(self, head: 'typing.Optional[Node]') -> 'typing.Optional[Node]':
        if not head:
            return None

        nodes = {}
        current = head

        while current:
            nodes[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            nodes[current].next = nodes[current.next] if current.next else None
            nodes[current].random = nodes[current.random] if current.random else None
            current = current.next

        return nodes[head]
