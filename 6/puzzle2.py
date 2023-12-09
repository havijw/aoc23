from math import ceil, floor


def get_races(filename: str) -> list[tuple[int]]:
    with open(filename, "r") as infile:
        time_line, dist_line, *_ = infile.readlines()
        _, *time_chars = time_line.split()
        time = int("".join(time_chars))
        _, *dist_chars = dist_line.split()
        dist = int("".join(dist_chars))
    return time, dist


def min_max_winners(race_time: int, record_dist: int) -> tuple[int, int]:
    equal_charge_time1 = (-race_time + (race_time**2 - 4 * record_dist) ** 0.5) / -2
    equal_charge_time2 = (-race_time - (race_time**2 - 4 * record_dist) ** 0.5) / -2
    min_equal_charge_time = min(equal_charge_time1, equal_charge_time2)
    max_equal_charge_time = max(equal_charge_time1, equal_charge_time2)
    return ceil(min_equal_charge_time), floor(max_equal_charge_time)


if __name__ == "__main__":
    time, dist = get_races("input.txt")
    min_winner, max_winner = min_max_winners(time, dist)
    num_winners = max_winner - min_winner + 1
    print(num_winners)
