class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result, indices = [], []

        for i, ch in enumerate(s):
            if ch.isalpha():
                result.append(ch)
            elif ch == "(":
                result.append("*")
                indices.append(i)
            else:
                if not indices:
                    result.append("*")
                    continue

                idx = indices.pop()
                result[idx] = "("
                result.append(")")

        return "".join([ch for ch in result if ch != "*"])
