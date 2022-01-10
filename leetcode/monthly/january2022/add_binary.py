class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = self.convert_binary_to_num(a), self.convert_binary_to_num(b)

        c = a + b

        result = []

        if c == 0:
            return "0"

        while c > 0:
            result.append(str(c % 2))
            c = c // 2

        return "".join(reversed(result))

    def convert_binary_to_num(self, a: str) -> int:
        result = 0
        pow = 0

        for i in range(len(a) - 1, -1, -1):
            if a[i] == '1':
                result += 2 ** pow

            pow += 1

        return result
