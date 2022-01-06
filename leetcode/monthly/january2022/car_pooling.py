from typing import List
import heapq

"""
=================
1094. Car Pooling
=================

=======
Problem
=======

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trip[i] = [numPassengers_i, from_i, to_i] indicates that
the ith trip has numPassengers_i passengers and the locations to pick them up and drop them off are from_i and to_i respectively. 
The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

========
Approach
========

For this problem, the most reasonable to start off doing is to sort the trips by the location passengers are picked up
in ascending order.

Once these trips are in ascending order, what I want to do is keep track of them using a priority queue where
the priority lies in the smallest end location. The reason we want to prioritize this is because we want to make sure
that we're letting passengers who need to be dropped off go which reduces our current_capacity.

So in the PoolTracker class, we have a function called add_trip which starts by popping the the smallest priority items
if the trip we're trying to add happens to have a start time greater than the end time of top of the priority queue.
The reason we want to do this is to make sure that we clear items from the priority queue that should have been dropped off
before letting more passengers in.

========
Analysis
========

This solution takes O(n lg n) time and O(n) space
"""


class PoolTracker:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_capacity = 0
        self.queue = []  # use a min-heap here

    def add_trip(self, trip: List[int]) -> bool:
        num_passengers, start, end = trip

        while self.queue and self.queue[0][1][2] <= start:
            current = heapq.heappop(self.queue)
            self.current_capacity -= current[1][0]

        if self.current_capacity + num_passengers > self.capacity:
            return False

        heapq.heappush(self.queue, (end, trip))
        self.current_capacity += num_passengers

        return True


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips or capacity == 0:
            return False

        trips = sorted(trips, key=lambda x: (x[1], x[2]))

        pool = PoolTracker(capacity)

        for trip in trips:
            if not pool.add_trip(trip):
                return False

        return True


if __name__ == "__main__":
    s = Solution()

    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4

    assert not s.carPooling(trips, capacity)

    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 5

    assert s.carPooling(trips, capacity)

    trips = [[2, 1, 5], [3, 5, 7]]
    capacity = 3

    assert s.carPooling(trips, capacity)

    trips = [[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]]
    capacity = 23

    assert s.carPooling(trips, capacity)

    trips = [[10, 5, 7], [10, 3, 4], [7, 1, 8], [6, 3, 4]]
    capacity = 24

    assert s.carPooling(trips, capacity)
