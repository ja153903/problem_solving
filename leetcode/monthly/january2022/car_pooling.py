from typing import List
import heapq


class PoolTracker:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_capacity = 0
        self.queue = []

    def add_trip(self, trip: List[int]) -> bool:
        num_passengers, start, _ = trip

        while self.queue and self.queue[0][1][2] <= start:
            current = heapq.heappop(self.queue)
            self.current_capacity -= current[1][0]

        if self.current_capacity + num_passengers > self.capacity:
            return False

        heapq.heappush(self.queue, (trip[2], trip))
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

    trips = [[10,5,7],[10,3,4],[7,1,8],[6,3,4]]
    capacity = 24

    assert s.carPooling(trips, capacity)
