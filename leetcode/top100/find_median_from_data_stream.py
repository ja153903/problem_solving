import collections
import heapq

from typing import List


class TLMedianFinder:
    def __init__(self):
        self.counter = collections.defaultdict(int)
        self.total_count = 0

    def _construct_list(self) -> List[int]:
        keys = sorted(list(self.counter.keys()))
        result = []

        for key in keys:
            for _ in range(self.counter[key]):
                result.append(key)

        return result

    def _get_median(self) -> float:
        sorted_list = self._construct_list()

        mid = self.total_count // 2

        if self.total_count % 2 == 1:
            return float(sorted_list[mid])

        return (sorted_list[mid] + sorted_list[mid - 1]) / 2

    def addNum(self, num: int) -> None:
        self.counter[num] += 1
        self.total_count += 1

    def findMedian(self) -> float:
        return self._get_median()


class MedianFinder:
    """
    The solution for this problem works with two heaps. One min heap and one max heap
    small is a max heap that contains the smaller half of the numbers
    large is a min heap that contains the larger half of the numbers

    this means that we always have access to the middle values
    """

    def __init__(self):
        self.small = []  # max-heap
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # the heaps are the same size, we opt to insert that value into the min heap
        # since our logic depends on the larger heap to have size (n/2 or n/2 + 1)
        if len(self.small) == len(self.large):
            # note that the number we get from the max heap will be negative so we have to negate it
            # before we insert it into the minheap
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            # if one is larger than the other, then this means that we have an odd
            # number of elements, so we can just return the top value of large
            return float(self.large[0])

        # remember that the value from the max-heap is going to be negative
        # that's why we're subtracting the value instead of adding it
        return float(self.large[0] - self.small[0]) / 2.0


if __name__ == '__main__':
    mf = MedianFinder()

    mf.addNum(1)
    mf.addNum(2)

    assert mf.findMedian() == 1.5

    mf.addNum(3)

    assert mf.findMedian() == 2.0
