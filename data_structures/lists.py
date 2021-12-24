import typing
import dataclasses


@dataclasses.dataclass
class ListNode:
    val: int = 0
    next: typing.Optional['ListNode'] = None


@dataclasses.dataclass
class Node:
    val: int
    next: typing.Optional['Node'] = None
    random: typing.Optional['Node'] = None
