import typing


class Solution:
    def exist(self, board: typing.List[typing.List[str]], word: str) -> bool:
        if not board or not word:
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    has_word = self.dfs(board, word, set(), 0, i, j)
                    if has_word:
                        return True

        return False

    def dfs(self, board: typing.List[typing.List[str]], word: str, visited: typing.Set[typing.Tuple[int, int]],
            index: int, row: int, col: int):
        # TODO: an optimization we can do here is to use a bitmask on the character on the board
        # instead of having to pass a copied set
        if index == len(word):
            return True

        if (
            (row, col) in visited or
            row < 0 or
            col < 0 or
            row >= len(board) or
            col >= len(board[0])
        ):
            return False

        if board[row][col] != word[index]:
            return False

        visited.add((row, col))

        return (
            self.dfs(board, word, visited.copy(), index + 1, row + 1, col) or
            self.dfs(board, word, visited.copy(), index + 1, row - 1, col) or
            self.dfs(board, word, visited.copy(), index + 1, row, col + 1) or
            self.dfs(board, word, visited.copy(), index + 1, row, col - 1)
        )


if __name__ == "__main__":
    s = Solution()

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    assert s.exist(board, word)

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"

    assert s.exist(board, word)

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"

    assert not s.exist(board, word)

    board = [["a"]]
    word = "a"

    assert s.exist(board, word)

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"

    assert s.exist(board, word)
