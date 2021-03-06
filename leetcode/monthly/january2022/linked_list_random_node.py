from typing import Optional
import random

from data_structures.lists import ListNode


"""
============================
382. Linked List Random Node
============================

=======
Problem
=======

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

* Solution(ListNode head) Initializes the object with the integer array nums.
* int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.

========
Approach
========

Note that getRandom will be called a lot.

Approach 1:
    We aren't adding any more values into the linked list
    We can uniformly sample these nodes once we load them into some list

Approach 2:
    Reservoir Sampling (Figure out how this works)
    https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling

    The basic idea here is that the problem we want to solve is the following:
        Choose k items from n total items with equal probability i.e. k/n

        To do this, we fill up a reservoir array with k elements
        We then pick the (k+1)th item with probability k/k+1
        In general, we pick the (k+i)th item with probability k/k+i
        We do this until k+i becomes n.

        Once we do this, we know have that these k items are randomly sampled with prob k/n
    
    In our case, k = 1

    So the solution should just be to initialize the reservoir as the head node.
    Then we should just iterate through the entire list (to sample all of it) so that
    we have uniform probability.

========
Analysis
========

This algorithm runs in O(n) time and O(1) space for getRandom()
"""


class LinearSpaceSolution:
    def __init__(self, head: Optional[ListNode]):
        self.nodes = []

        while head:
            self.nodes.append(head)
            head = head.next

    def getRandom(self) -> int:
        return self.nodes[int(random.random() * len(self.nodes))].val


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        curr = self.head
        ans = self.head
        i = 1

        while curr:
            if random.random() < 1 / i:
                ans = curr

            curr = curr.next
            i += 1

        return ans.val
