from typing import Optional


from data_structures.lists import ListNode
from algorithms.lists import (
    create_linked_list_from_list,
    create_list_from_linked_list,
)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result, stack, i = [], [], 0

        while head:
            while i < k and head:
                stack.append(head)
                head = head.next
                i += 1

            if len(stack) < k:
                for item in stack:
                    result.append(item)
            else:
                while stack:
                    result.append(stack.pop())

            i = 0

        root = ListNode()
        runner = root

        for node in result:
            runner.next = node
            runner = runner.next

        if runner:
            runner.next = None

        return root.next


if __name__ == '__main__':
    s = Solution()

    root = create_linked_list_from_list([1, 2, 3, 4, 5])
    res = s.reverseKGroup(root, 2)

    print(create_list_from_linked_list(res))

    root = create_linked_list_from_list([1, 2, 3, 4, 5])
    res = s.reverseKGroup(root, 3)

    print(create_list_from_linked_list(res))

    root = create_linked_list_from_list([1, 2])
    res = s.reverseKGroup(root, 2)

    print(create_list_from_linked_list(res))
