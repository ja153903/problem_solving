import collections
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # This problem is basically two sum after we normalize
        # all values by modulo 60
        freq = collections.defaultdict(int)
        mod = [t % 60 for t in time]

        result = 0

        for t in mod:
            if t == 0 and t in freq:
                result += freq[0]
            elif 60 - t in freq:
                result += freq[60 - t]

            freq[t] += 1

        return result


    def brute_force(self, time: List[int]) -> int:
        n = len(time)
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                if (time[i] + time[j]) % 60 == 0:
                    result += 1

        return result


if __name__ == "__main__":
    s = Solution()

    # Test Brute Force
    time = [30, 20, 150, 100, 40]
    assert s.brute_force(time) == 3
    assert s.numPairsDivisibleBy60(time) == 3

    time = [30, 30, 30]
    assert s.brute_force(time) == 3
    assert s.numPairsDivisibleBy60(time) == 3

    time = [60, 60, 60]
    assert s.brute_force(time) == 3
    assert s.numPairsDivisibleBy60(time) == 3
