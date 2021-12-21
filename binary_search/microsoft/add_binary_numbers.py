class Solution:
    def solve(self, a, b):
        result = []
        carry = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 and j >= 0:
            current = carry

            if a[i] == '1':
                current += 1

            i -= 1

            if b[j] == '1':
                current += 1

            j -= 1

            result.append(current % 2)
            carry = current // 2

        while i >= 0:
            current = carry

            if a[i] == '1':
                current += 1

            i -= 1

            result.append(current % 2)
            carry = current // 2

        while j >= 0:
            current = carry

            if b[j] == '1':
                current += 1

            j -= 1

            result.append(current % 2)
            carry = current // 2

        if carry:
            result.append(carry)

        return ''.join([str(i) for i in reversed(result)])