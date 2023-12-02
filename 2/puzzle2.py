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

    @property
    def power(self) -> int:
        return max(self.red) * max(self.green) * max(self.blue)

    @classmethod
    def from_line(cls, line: str) -> "Game":
        line_id = int(Game.linestart.match(line).group("line_id"))
        draws = {"red": [], "green": [], "blue": []}
        for draw in Game.draw.finditer(line):
            draws[draw.group("color")].append(int(draw.group("num")))
        return cls(line_id, **draws)


if __name__ == "__main__":
    games = map(Game.from_line, get_input("input.txt"))
    print(sum(game.power for game in games))
