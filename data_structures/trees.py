import typing
import dataclasses


@dataclasses.dataclass
class TreeNode:
    val: int = 0
    left: typing.Optional['TreeNode'] = None
    right: typing.Optional['TreeNode'] = None
