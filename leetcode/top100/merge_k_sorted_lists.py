import typing
import heapq

from data_structures.lists import ListNode
from algorithms.lists import create_linked_list_from_list, create_list_from_linked_list


class Solution:
    def mergeKLists(self, lists: typing.List[typing.Optional[ListNode]]) -> typing.Optional[ListNode]:
        heap = []

        # there are going to be k elements
        while True:
            null_node_cnt = 0
            for i, _list in enumerate(lists):
                if _list is None:
                    null_node_cnt += 1
                    continue

                heapq.heappush(heap, _list.val)
                lists[i] = lists[i].next

            if null_node_cnt == len(lists):
                break

        root = ListNode()
        runner = root

        while heap:
            runner.next = ListNode(heapq.heappop(heap))
            runner = runner.next

        return root.next


if __name__ == '__main__':
    s = Solution()

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    nodes = [create_linked_list_from_list(lst) for lst in lists]

    res = s.mergeKLists(nodes)

    print(create_list_from_linked_list(res))
