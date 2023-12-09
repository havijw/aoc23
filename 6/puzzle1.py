def get_races(filename: str) -> list[tuple[int]]:
    with open(filename, "r") as infile:
        times, dists, *_ = infile.readlines()
        _, *times = times.split()
        times = [int(t) for t in times]
        _, *dists = dists.split()
        dists = [int(d) for d in dists]
    return times, dists


def min_max_winners(race_time: int, record_dist: int) -> tuple[int, int]:
    def race_dist(charge_time: int) -> int:
        return (race_time - charge_time) * charge_time

    winners = [t for t in range(race_time) if race_dist(t) > record_dist]
    return min(winners), max(winners)


if __name__ == "__main__":
    times, dists = get_races("input.txt")
    total_prod = 1
    for t, d in zip(times, dists):
        min_winner, max_winner = min_max_winners(t, d)
        num_winners = max_winner - min_winner + 1
        total_prod *= num_winners
    print(total_prod)
