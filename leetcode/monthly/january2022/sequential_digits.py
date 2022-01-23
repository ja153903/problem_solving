from typing import List
from collections import deque


class Solution:
    def generate_sequence(self, size: int) -> int:
        d = deque()

        for i in range(size):
            d.append(i + 1)

        while d:
            yield int("".join([str(d[i]) for i in range(size)]))

            d.popleft()
            if d[-1] != 9:
                d.append(d[-1] + 1)
            else:
                break

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        min_len = len(str(low))
        max_len = len(str(high))

        for length in range(min_len, max_len + 1):
            for seq in self.generate_sequence(length):
                if seq > high:
                    break

                if low <= seq <= high:
                    result.append(seq)

        return result
        
