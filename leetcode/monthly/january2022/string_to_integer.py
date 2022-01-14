class Solution:
    def myAtoi(self, s: str) -> int:
        stack = []
        is_neg = False

        i = 0

        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            is_neg = True if s[i] == "-" else False
            i += 1

        while i < len(s) and s[i].isdigit():
            stack.append(s[i])
            i += 1

        neg_clamped = -2 ** 31
        pos_clamped = 2 ** 31 - 1

        try:
            num = int("".join(stack))
            if neg_clamped <= num <= pos_clamped:
                return -num if is_neg else num
            else:
                return neg_clamped if is_neg else pos_clamped
        except:
            return 0



if __name__ == "__main__":
    s = Solution()

    assert s.myAtoi("42") == 42
    assert s.myAtoi("         -42") == -42
    assert s.myAtoi("4193 with words") == 4193
