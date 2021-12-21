import typing

from data_structures.lists import ListNode


def create_linked_list_from_list(lst: typing.List[int]) -> typing.Optional[ListNode]:
    if not lst:
        return None

    root = ListNode()
    runner = root

    for num in lst:
        runner.next = ListNode(val=num)
        runner = runner.next

    return root.next


def create_list_from_linked_list(root: typing.Optional[ListNode]) -> typing.List[int]:
    result = []

    while root:
        result.append(root.val)
        root = root.next

    return result
