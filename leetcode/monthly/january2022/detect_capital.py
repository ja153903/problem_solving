class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        num_capital = 0

        for ch in word:
            if ch.isupper():
                num_capital += 1

        all_capital = num_capital == len(word)
        no_capital = num_capital == 0
        first_capital = word[0].isupper() and num_capital == 1

        return all_capital or no_capital or first_capital
