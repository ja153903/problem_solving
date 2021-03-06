"""
139. Word Break

=======
Problem
=======

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

========
Approach
========

Recursive approach:
    Base case:
        if the string is at the end, return true if the word exists within the dictionary else false

    Step:
        at every step, the decision we always make is to add on another character to the string.
        however, if the current string we have exists within the dictionary, then we start with a new string.

    However, this solution will timeout.

DP Approach:
    How can we optimize the above recursion?

    We can let dp[i] for some i in [0, len(s) -1], be the ability to construct
    a string up to and not including index i
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_set = set(word_dict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]

    def word_break_recursive(self, s: str, word_dict: List[str]) -> bool:
        word_set = set(word_dict)

        def rec(word: str, index: int, current: str) -> bool:
            if index == len(word) - 1:
                return f"{current}{word[index]}" in word_set

            result = False

            if f"{current}{word[index]}" in word_set:
                result |= rec(word, index + 1, "")

            result |= rec(word, index + 1, f"{current}{word[index]}")

            return result

        return rec(s, 0, "")


if __name__ == "__main__":
    s = Solution()

    assert s.word_break_recursive("leetcode", ["leet", "code"])
    assert s.word_break_recursive("applepenapple", ["apple", "pen"])
    assert not s.word_break_recursive(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]
    )
