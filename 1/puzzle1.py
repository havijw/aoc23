def get_input() -> list[str]:
    with open("input.txt", "r") as infile:
        return [line for line in infile]


def parse_calibration(line: str) -> int:
    digits = [int(c) for c in line if c.isdigit()]
    return 10 * digits[0] + digits[-1]


if __name__ == "__main__":
    input_lines = get_input()
    print(sum(map(parse_calibration, input_lines)))
