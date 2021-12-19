from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Instruction:
    start: Point
    end: Point
    command: str


def parse_file() -> List[Instruction]:
    result = []

    with open('data/day6.txt', 'r') as f:
        for line in f:
            by_whitespace = line.split(' ')
            by_comma = [component for component in by_whitespace if ',' in component]

            start_as_str, end_as_str = by_comma

            start_x, start_y = start_as_str.split(',')
            end_x, end_y = end_as_str.split(',')

            start = Point(x=int(start_x), y=int(start_y))
            end = Point(x=int(end_x), y=int(end_y))

            if by_whitespace[0] == 'toggle':
                command = 'toggle'
            elif by_whitespace[1] == 'on':
                command = 'on'
            else:
                command = 'off'

            result.append(Instruction(start=start, end=end, command=command))

    return result


def part1() -> None:
    instructions = parse_file()

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        command = instruction.command
        start = instruction.start
        end = instruction.end

        match command:
            case 'toggle':
                toggle(grid, start, end)
            case 'on':
                turn_on(grid, start, end)
            case 'off':
                turn_off(grid, start, end)

    count = count_lit(grid)

    print(count)


def part2() -> None:
    instructions = parse_file()

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in instructions:
        command = instruction.command
        start = instruction.start
        end = instruction.end

        match command:
            case 'toggle':
                toggle(grid, start, end, True)
            case 'on':
                turn_on(grid, start, end, True)
            case 'off':
                turn_off(grid, start, end, True)

    count = count_lit(grid)

    print(count)


def toggle(grid: List[List[int]], start: Point, end: Point, is_part2: bool = False):
    for i in range(start.y, end.y + 1):
        for j in range(start.x, end.x + 1):
            if not is_part2:
                grid[i][j] = 1 if grid[i][j] == 0 else 0
            else:
                grid[i][j] += 2


def turn_on(grid: List[List[int]], start: Point, end: Point, is_part2: bool = False):
    for i in range(start.y, end.y + 1):
        for j in range(start.x, end.x + 1):
            if not is_part2:
                grid[i][j] = 1
            else:
                grid[i][j] += 1


def turn_off(grid: List[List[int]], start: Point, end: Point, is_part2: bool = False):
    for i in range(start.y, end.y + 1):
        for j in range(start.x, end.x + 1):
            if not is_part2:
                grid[i][j] = 0
            else:
                grid[i][j] = max(0, grid[i][j] - 1)


def count_lit(grid: List[List[int]]) -> int:
    return sum(sum(row) for row in grid)


if __name__ == '__main__':
    part1()
    part2()
