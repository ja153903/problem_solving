from typing import Optional

from data_structures.lists import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        runnerA, runnerB = headA, headB

        while runnerA or runnerB:
            if runnerA == runnerB:
                return runnerA

            if runnerA:
                runnerA = runnerA.next
            else:
                runnerA = headB

            if runnerB:
                runnerB = runnerB.next
            else:
                runnerB = headA

        return None
