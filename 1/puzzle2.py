from puzzle1 import get_input

word_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
digits = list(map(str, range(1, 10)))


def parse_calibration(line: str) -> int:
    line_digits = []
    for i in range(len(line)):
        if line[i] in digits:
            line_digits.append(int(line[i]))
        else:
            for s in word_to_num:
                if line[i:].startswith(s):
                    line_digits.append(word_to_num[s])
                    break

    res = 10 * line_digits[0] + line_digits[-1]
    return res


if __name__ == "__main__":
    input_lines = get_input("input.txt")
    print(sum(map(parse_calibration, input_lines)))
