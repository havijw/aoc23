def num_winning_nums(line: str) -> int:
    card_num, numbers = line.split(": ")
    winning, mine = numbers.split("|")
    winning_nums = [int(n) for n in winning.split(" ") if n != ""]
    my_nums = [int(n) for n in mine.split(" ") if n != ""]
    my_winning_nums = [n for n in my_nums if n in winning_nums]
    return len(my_winning_nums)


with open("input.txt") as infile:
    lines = [line for line in infile]
    copies = {i: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        winners = num_winning_nums(line)
        for j in range(i + 1, i + 1 + winners):
            if j < len(copies):
                copies[j] += copies[i]
    print(sum(copies.values()))
