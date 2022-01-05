from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        self.backtrack(s, result, [s[0]], 1)

        return result

    def backtrack(self, s: str, result: List[List[str]], current: List[str], index: int) -> None:
        if index == len(s):
            for word in current:
                if not self.is_palindrome(word):
                    return

            result.append(list(current))
        else:
            # we can choose to add this as its own element
            # we can also choose to add it to the top of the current list
            option_one = list(current) + [s[index]]
            self.backtrack(s, result, option_one, index + 1)
            option_two = list(current)
            option_two[-1] += s[index]
            self.backtrack(s, result, option_two, index + 1)


    def is_palindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    s = Solution()

    print(s.partition("aab"))
    print(s.partition("a"))
