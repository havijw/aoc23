import re
from dataclasses import dataclass


def get_input(filename: str) -> list[str]:
    with open(filename, "r") as infile:
        return [line for line in infile]


@dataclass
class Game:
    line_id: int
    red: list[int]
    green: list[int]
    blue: list[int]

    linestart = re.compile(r"^Game (?P<line_id>\d*): ")
    draw = re.compile(r"(?P<num>\d+) (?P<color>blue|red|green)(, |;|$)")

    def valid(self) -> bool:
        return max(self.red) <= 12 and max(self.green) <= 13 and max(self.blue) <= 14

    @classmethod
    def from_line(cls, line: str) -> "Game":
        line_id = int(Game.linestart.match(line).group("line_id"))
        draws = {"red": [0], "green": [0], "blue": [0]}
        for draw in Game.draw.finditer(line):
            draws[draw.group("color")].append(int(draw.group("num")))
        return cls(line_id, **draws)


if __name__ == "__main__":
    games = map(Game.from_line, get_input("input.txt"))
    valid_games = filter(Game.valid, games)
    print(sum((game.line_id for game in valid_games)))
