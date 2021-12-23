import typing
import heapq
import collections


class Solution:
    def maxSlidingWindow(self, nums: typing.List[int], k: int) -> typing.List[int]:
        # we keep track of the indices of potential candidates
        queue = collections.deque()
        result = []

        for i, num in enumerate(nums):
            # while the back of the queue is smaller than the current number
            # we remove that element (this is because we want to weed out
            # candidates that won't make sense)
            while queue and nums[queue[-1]] < num:
                queue.pop()

            # add the current index
            queue.append(i)

            # if the previous index is past the current range for
            # the sliding window, we get rid of it.
            if queue[0] == i - k:
                queue.popleft()

            # if we're at the end of the sliding window, we add the value in front
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result

    def max_heap_tle(self, nums: typing.List[int], k: int) -> typing.List[int]:
        result = []
        max_heap = []

        begin, end = 0, 0

        while end < len(nums):
            while len(max_heap) < k:
                heapq.heappush(max_heap, -nums[end])
                end += 1

            result.append(-max_heap[0])
            max_heap.remove(-nums[begin])

            begin += 1

        return result


if __name__ == '__main__':
    s = Solution()

    assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert s.maxSlidingWindow([1], 1) == [1]
    assert s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]
