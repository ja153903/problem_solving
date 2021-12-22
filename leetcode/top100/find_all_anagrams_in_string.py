import collections
import typing


class Solution:
    def is_anagram(self, s: str, p: str) -> bool:
        return sorted(s) == sorted(p)

    def brute_force(self, s: str, p: str) -> typing.List[int]:
        if len(p) > len(s):
            return []

        p_len = len(p)

        result = []

        for i in range(0, len(s) - p_len + 1):
            if self.is_anagram(s[i:i + p_len], p):
                result.append(i)

        return result

    def is_anagram_optimal(self, s: str, p: str) -> bool:
        counter = collections.Counter(p)

        for ch in s:
            if ch not in counter:
                return False

            if counter[ch] == 0:
                return False

            counter[ch] -= 1

        return sum(counter.values()) == 0

    def still_brute_force(self, s: str, p: str) -> typing.List[int]:
        if len(p) > len(s):
            return []

        p_len = len(p)

        result = []

        for i in range(0, len(s) - p_len + 1):
            if self.is_anagram_optimal(s[i:i + p_len], p):
                result.append(i)

        return result

    def findAnagrams(self, s: str, p: str) -> typing.List[int]:
        result = []
        p_counter = collections.Counter(p)

        counter = len(p_counter)

        begin, end = 0, 0

        while end < len(s):
            ch = s[end]

            if ch in p_counter:
                p_counter[ch] -= 1
                if p_counter[ch] == 0:
                    counter -= 1

            end += 1

            while counter == 0:
                temp = s[begin]
                if temp in p_counter:
                    p_counter[temp] += 1
                    if p_counter[temp] > 0:
                        counter += 1
                if end - begin == len(p):
                    result.append(begin)

                begin += 1

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert s.findAnagrams("abab", "ab") == [0, 1, 2]
