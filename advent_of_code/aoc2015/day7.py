from __future__ import annotations

import collections
from dataclasses import dataclass
from typing import DefaultDict, List, Optional, TypedDict, Callable, Any


@dataclass
class Command:
    args: List[str]
    dst: str
    instruction: Optional[str] = None


class ParseResult(TypedDict):
    commands: List[Command]
    wires: DefaultDict[str, int]


def parse_file() -> ParseResult:
    commands = []
    wires = collections.defaultdict(int)

    with open('data/day7.txt', 'r') as f:
        for line in f:
            parts = line.rstrip('\n').split(' ')

            match len(parts):
                case 3:
                    try:
                        wires[parts[-1]] = int(parts[0])
                    except ValueError:
                        command = Command(
                            instruction='ADD',
                            args=[parts[0]],
                            dst=parts[-1]
                        )
                        commands.append(command)
                case 4:
                    command = Command(
                        instruction=parts[0],
                        args=[parts[1]],
                        dst=parts[-1]
                    )
                    commands.append(command)
                case 5:
                    command = Command(
                        instruction=parts[1],
                        args=[parts[0], parts[2]],
                        dst=parts[-1]
                    )
                    commands.append(command)

    return {'commands': commands, 'wires': wires}


def execute_commands(commands: List[Command], wires: DefaultDict[str, int]) -> None:
    while commands:
        used_commands = set()
        for i, command in enumerate(commands):
            args = command.args
            dst = command.dst
            instruction = command.instruction

            match instruction:
                case 'ADD':
                    arg = args[0]
                    if arg not in wires:
                        continue

                    wires[dst] = wires.get(arg)
                case 'NOT':
                    arg = args[0]
                    if arg not in wires:
                        continue

                    wires[dst] = ~wires[arg] & 65535
                case 'AND' | 'OR':
                    a, b = args

                    parse_int: Callable[[str], int | None] = \
                        lambda s: wires.get(s) if not s.isdigit() else int(s)

                    a = parse_int(a)
                    b = parse_int(b)

                    if a is None or b is None:
                        continue

                    if instruction == 'AND':
                        wires[dst] = a & b
                    else:
                        wires[dst] = a | b
                case 'LSHIFT' | 'RSHIFT':
                    a, b = args
                    if a not in wires:
                        continue

                    if instruction == 'LSHIFT':
                        wires[dst] = wires[a] << int(b)
                    else:
                        wires[dst] = wires[a] >> int(b)

            used_commands.add(i)

        commands = [command for i, command in enumerate(commands) if i not in used_commands]


def part1() -> None:
    result = parse_file()
    commands = result.get('commands', [])
    wires = result.get('wires', {})

    execute_commands(commands, wires)

    print(wires.get('a'))


def part2() -> None:
    result = parse_file()
    commands = result.get('commands', [])
    wires = result.get('wires', {})

    wires['a'] = 3176
    wires['b'] = wires['a']

    execute_commands(commands, wires)

    print(wires.get('a'))


if __name__ == '__main__':
    part1()
    part2()
