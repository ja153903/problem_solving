from typing import Optional
from data_structures.tries import Trie, TrieNode


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        # for each character, if that character is an alphabetic character
        # then we just search the children for that value.
        # else if the character is a dot, then we have to go through each child
        runner = self.trie.head
        self.res = False
        self._dfs(runner, word, 0)

        return self.res

    def _dfs(self, runner: Optional[TrieNode], word: str, index: int) -> None:
        if index == len(word):
            if runner and runner.is_end:
                self.res = True
            return
        elif not runner:
            return
        else:
            if word[index] == ".":
                for child in runner.children:
                    self._dfs(child, word, index + 1)
            else:
                exists = False
                next_child = None

                for child in runner.children:
                    if child and child.value == word[index]:
                        exists = True
                        next_child = child
                        break

                if exists:
                    self._dfs(next_child, word, index + 1)
