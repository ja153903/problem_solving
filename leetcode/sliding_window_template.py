import typing
import collections


class Solution:
    def sliding_window_template(self, s: str, t: str) -> typing.List[int]:
        # create a collection or int value to save the result according the question.
        result = []
        if len(t) > len(s):
            return result

        # create a counter to save the characters of the target substring
        counter = collections.Counter(t)

        # maintain a counter to check if it matches the target string length
        count = len(counter)

        # two pointers; begin - left pointer of the window; end - right pointer of the window
        begin, end = 0, 0

        while end < len(s):
            c = s[end]

            if c in counter:
                counter[c] -= 1
                if counter[c] == 0:
                    count -= 1

            end += 1

            while count == 0:
                temp = s[begin]
                if temp in counter:
                    counter[temp] += 1
                    if counter[temp] > 0:
                        count += 1

                begin += 1

        return result
