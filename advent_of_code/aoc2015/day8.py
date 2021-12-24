import typing


def parse_file() -> typing.List[str]:
    result = []

    with open("data/day8-example.txt", "r") as file:
        for line in file:
            result.append(line.rstrip("\n"))

        return result


def part1() -> None:
    lines = parse_file()
    result = 0
    for line in lines:
        num_chars = len(line)
        num_in_memory = 0

        i = 1
        while i < num_chars - 1:
            if line[i] == "x":
                if line[i - 1] == "\\":
                    num_in_memory += 1
                    i += 3
                else:
                    num_in_memory += 1
                    i += 1
            elif line[i] == "\\":
                i += 1
            else:
                num_in_memory += 1
                i += 1

        print(f"{line}: {num_chars} chars and {num_in_memory} in memory")
        result += num_chars - num_in_memory

    print(result)


if __name__ == "__main__":
    part1()
