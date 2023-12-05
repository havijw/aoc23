def value(line: str) -> int:
    card_num, numbers = line.split(": ")
    winning, mine = numbers.split("|")
    winning_nums = [int(n) for n in winning.split(" ") if n != ""]
    my_nums = [int(n) for n in mine.split(" ") if n != ""]
    my_winning_nums = [n for n in my_nums if n in winning_nums]
    return int(0.5 * 2 ** len(my_winning_nums))


with open("input.txt") as infile:
    total_value = 0
    for line in infile:
        total_value += value(line)
    print(total_value)
