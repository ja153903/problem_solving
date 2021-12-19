def parse_file() -> str:
    result = []

    with open('data/day3.txt', 'r') as f:
        for line in f:
            result.append(line)

    return ''.join(result)


DIR_MAP = {
    '^': [0, -1],
    'v': [0, 1],
    '>': [1, 0],
    '<': [-1, 0]
}


def part1() -> None:
    directions = parse_file()

    visited = set()
    x, y = 0, 0

    visited.add(f'{x},{y}')

    for direction in directions:
        dx, dy = DIR_MAP[direction]
        x, y = x + dx, y + dy

        as_str = f'{x},{y}'
        if as_str in visited:
            continue

        visited.add(as_str)

    print(len(visited))


def part2() -> None:
    directions = parse_file()

    visited = set()
    sx, sy = 0, 0
    rx, ry = 0, 0

    visited.add(f'{rx},{ry}')

    for i in range(0, len(directions), 2):
        sdx, sdy = DIR_MAP[directions[i]]
        rdx, rdy = DIR_MAP[directions[i + 1]]

        sx, sy = sx + sdx, sy + sdy
        rx, ry = rx + rdx, ry + rdy

        flesh_as_str = f'{sx},{sy}'
        robo_as_str = f'{rx},{ry}'

        visited.add(flesh_as_str)
        visited.add(robo_as_str)

    print(len(visited))


if __name__ == '__main__':
    part1()
    part2()
