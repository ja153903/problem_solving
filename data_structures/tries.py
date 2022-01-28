from typing import Optional, List
from dataclasses import dataclass


@dataclass
class TrieNode:
    value: str
    children: List[Optional["TrieNode"]]
    is_end: bool = False


class Trie:
    def __init__(self):
        self.head = TrieNode(value="", children=[])

    def insert(self, word: str) -> None:
        runner = self.head

        for ch in word:
            if not runner.children:
                node = TrieNode(value=ch, children=[])
                runner.children.append(node)
                runner = node
            else:
                for child in runner.children:
                    if child and child.value == ch:
                        runner = child

        runner.is_end = True
        runner.children.append(None)
