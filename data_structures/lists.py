import typing
import dataclasses


@dataclasses.dataclass
class ListNode:
    val: int = 0
    next: typing.Optional['ListNode'] = None
