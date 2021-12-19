def parse_file():
    result = []

    with open('data/day1.txt', 'r') as f:
        for line in f:
            result.append(line)

    return ''.join(result)


def part1():
    lisp = parse_file()
    pos = 0

    for ch in lisp:
        if ch == '(':
            pos += 1

        if ch == ')':
            pos -= 1

    print(pos)


def part2():
    lisp = parse_file()
    pos = 0

    for i, ch in enumerate(lisp):
        if ch == '(':
            pos += 1

        if ch == ')':
            pos -= 1

        if pos == -1:
            print(i)
            break


part1()
part2()
