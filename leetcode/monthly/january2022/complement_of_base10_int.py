class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        bits = []

        while n > 0:
            bits.append(n % 2)
            n = n // 2

        complement = [1 if i == 0 else 0 for i in bits]

        result = 0
        for i in range(0, len(complement)):
            result += complement[i] * (2 ** i)

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.bitwiseComplement(5) == 2
    assert s.bitwiseComplement(7) == 0
    assert s.bitwiseComplement(10) == 5
    assert s.bitwiseComplement(0) == 1
