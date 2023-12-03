import re

from puzzle1 import get_engine_schematic, number_regex


def surrounding_numbers(grid: list[str], row: int, col: int) -> list[int]:
    surrounding = []
    left_bound = max(0, col - 1)
    right_bound = min(len(grid[0]) - 1, col + 1)
    if row > 0:
        for m in number_regex.finditer(grid[row - 1]):
            if (
                left_bound <= m.start() <= right_bound
                or left_bound <= m.end() - 1 <= right_bound
            ):
                surrounding.append(int(grid[row - 1][m.start() : m.end()]))
    if row < len(grid) - 1:
        for m in number_regex.finditer(grid[row + 1]):
            if (
                left_bound <= m.start() <= right_bound
                or left_bound <= m.end() - 1 <= right_bound
            ):
                surrounding.append(int(grid[row + 1][m.start() : m.end()]))
    for m in number_regex.finditer(grid[row]):
        if m.start() == right_bound or m.end() - 1 == left_bound:
            surrounding.append(int(grid[row][m.start() : m.end()]))
    return surrounding


def gear_ratio(grid: list[str], row: int, col: int) -> int:
    gears = surrounding_numbers(grid, row, col)
    if grid[row][col] == "*" and len(gears) == 2:
        return gears[0] * gears[1]
    else:
        return 0


if __name__ == "__main__":
    grid = get_engine_schematic("input.txt")
    print(
        sum(
            (
                gear_ratio(grid, r, c)
                for r, row in enumerate(grid)
                for c, col in enumerate(row)
            )
        )
    )
