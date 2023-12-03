import re


def get_engine_schematic(filename: str) -> list[str]:
    with open(filename, "r") as infile:
        return [line[:-1] for line in infile]


def surrounding_rect(
    grid: list[str], row: int, start_col: int, end_col: int
) -> list[str]:
    """
    Rectangle surrounding the 1 x length rectangle grid[row][start : end]

    Returns 1D list of elements
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    # inclusive bounds
    left_bound = max(start_col - 1, 0)
    right_bound = min(end_col, n_cols - 1)

    elements = []
    if row > 0:
        elements.extend(grid[row - 1][left_bound : right_bound + 1])
    if start_col > 0:
        elements.append(grid[row][start_col - 1])
    if end_col < n_cols:
        elements.append(grid[row][end_col])
    if row < n_rows - 1:
        elements.extend(grid[row + 1][left_bound : right_bound + 1])
    return elements


def adjacent_to_symbol(grid: list[str], row: int, start_col: int, end_col: int) -> bool:
    return any(
        not c.isdigit() and c != "."
        for c in surrounding_rect(grid, row, start_col, end_col)
    )


number_regex = re.compile(r"\d+")


def number_locations(grid: list[str]) -> list[tuple[int, int, int]]:
    """
    Tuples of (row, start, end) for each number in grid
    """
    locations = []
    for row_index, row in enumerate(grid):
        locations.extend(
            ((row_index, m.start(), m.end()) for m in number_regex.finditer(row))
        )
    return locations


if __name__ == "__main__":
    grid = get_engine_schematic("input.txt")
    assert all((len(row) == len(grid[0]) for row in grid))
    included_locations = [
        (row, start_col, end_col)
        for row, start_col, end_col in number_locations(grid)
        if adjacent_to_symbol(grid, row, start_col, end_col)
    ]
    included_numbers = [
        int("".join(grid[row][start_col:end_col]))
        for row, start_col, end_col in included_locations
    ]
    print(sum(included_numbers))
