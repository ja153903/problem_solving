from typing import List


def parse_file() -> List[str]:
    result = []

    with open('data/day5.txt') as f:
        for line in f:
            result.append(line.rstrip('\n'))

    return result


def is_nice(s: str) -> bool:
    return (
            vowels__lte_3(s) and
            substr__dup(s) and
            substr__does_not_contain(s)
    )


def vowels__lte_3(s: str) -> bool:
    count = 0

    for ch in s:
        if ch in 'aeiou':
            count += 1

    return count >= 3


def substr__dup(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return True

    return False


def substr__does_not_contain(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i - 1: i + 1] in ['ab', 'cd', 'pq', 'xy']:
            return False

    return True


def part1() -> None:
    lines = parse_file()

    result = [
        line for line in lines
        if is_nice(line)
    ]

    print(len(result))


def is_new_nice(s: str) -> bool:
    return (
            pairs__appears_lte_2(s) and
            repeats__within_char(s)
    )


def pairs__appears_lte_2(s: str) -> bool:
    for i in range(len(s) - 3):
        pair = s[i:i + 2]
        if pair in s[i + 2:]:
            return True

    return False


def repeats__within_char(s: str) -> bool:
    for i in range(1, len(s) - 1):
        if s[i - 1] == s[i + 1]:
            return True

    return False


def part2() -> None:
    lines = parse_file()

    result = [
        line for line in lines
        if is_new_nice(line)
    ]

    print(len(result))


if __name__ == '__main__':
    part1()
    part2()
