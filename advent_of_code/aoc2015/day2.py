from dataclasses import dataclass
from typing import List


@dataclass
class Dimensions:
    length: int
    width: int
    height: int

    @property
    def surface_area(self) -> int:
        return (
            2 * self.length * self.width +
            2 * self.width * self.height +
            2 * self.height * self.length
        )

    @property
    def area_of_smallest_side(self) -> int:
        return min([
            self.height * self.length,
            self.height * self.width,
            self.length * self.width,
        ])

    @property
    def sqft(self) -> int:
        return self.surface_area + self.area_of_smallest_side

    @property
    def perimeter_of_smallest_side(self) -> int:
        return min([
            2 * self.height + 2 * self.length,
            2 * self.height + 2 * self.width,
            2 * self.length + 2 * self.width,
        ])

    @property
    def volume(self) -> int:
        return self.width * self.length * self.height

    @property
    def ribbon_length(self) -> int:
        return self.volume + self.perimeter_of_smallest_side


def parse_file() -> List[Dimensions]:
    result = []

    with open('data/day2.txt', 'r') as f:
        for line in f:
            l, w, h = line.split('x')
            result.append(Dimensions(length=int(l), width=int(w), height=int(h)))

    return result


def part1() -> None:
    dimensions = parse_file()
    solution = sum(dimension.sqft for dimension in dimensions)
    print(solution)


def part2() -> None:
    dimensions = parse_file()
    solution = sum(dimension.ribbon_length for dimension in dimensions)
    print(solution)


if __name__ == '__main__':
    part1()
    part2()
