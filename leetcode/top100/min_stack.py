import typing


class MinStack:
    def __init__(self):
        self.stack: typing.List[typing.Tuple[int, int]] = []

    def push(self, val: int) -> None:
        if self.stack:
            current_min = min(val, self.getMin())
        else:
            current_min = val

        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    assert stack.getMin() == -3