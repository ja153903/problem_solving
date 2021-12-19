import hashlib


def encode_secret_key(sauce: int) -> str:
    secret_key = f'iwrupvqb{sauce}'

    encoded = hashlib.md5(secret_key.encode())

    return encoded.hexdigest()


def starts_with(s: str, t: str) -> bool:
    return t == s[:len(t)]


def part1() -> None:
    i = 1

    while not starts_with(encode_secret_key(i), '00000'):
        i += 1

    print(i)


def part2() -> None:
    i = 1

    while not starts_with(encode_secret_key(i), '000000'):
        i += 1

    print(i)


if __name__ == '__main__':
    part1()
    part2()
