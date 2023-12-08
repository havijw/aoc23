class MapRange:
    def __init__(self, dst_start: int, src_start: int, length: int):
        self.dst_start = dst_start
        self.src_start = src_start
        self.length = length

    def __contains__(self, n: int) -> bool:
        return self.src_start <= n < self.src_start + self.length

    def __len__(self) -> int:
        return self.length

    def __call__(self, n: int) -> int:
        if n in self:
            return n - self.src_start + self.dst_start
        return n


class Map:
    def __init__(
        self, source: str, destination: str, ranges: list[tuple[int, int, int]]
    ):
        self.src = source
        self.dst = destination
        self.map_ranges: list[MapRange] = [
            MapRange(dst_start, src_start, length)
            for dst_start, src_start, length in ranges
        ]

    def __call__(self, n: int) -> int:
        for map_range in self.map_ranges:
            if n in map_range:
                return map_range(n)
        return n

    @classmethod
    def from_lines(cls, lines: list[str]) -> "Map":
        source_line, *range_lines = lines

        # parse source and destination
        src_to_dst, _ = source_line.split(" ")
        src, dst = src_to_dst.split("-to-")

        # parse map ranges
        ranges = []
        for line in range_lines:
            ranges.append(tuple(map(int, line.split(" "))))

        return cls(src, dst, ranges)


def get_seeds_and_maps(filename: str) -> tuple[list[int], list[Map]]:
    with open(filename, "r") as infile:
        seeds_line, _, *map_lines = [line[:-1] for line in infile.readlines()]

        # parse seeds
        _, *seeds = seeds_line.split(" ")
        seeds = [int(seed) for seed in seeds]

        # parse maps
        maps = []
        currmap = []
        i = 0
        while i < len(map_lines):
            currmap.append(map_lines[i])
            i += 1
            while i < len(map_lines) and "map" not in map_lines[i]:
                currmap.append(map_lines[i])
                i += 1
            maps.append(Map.from_lines(currmap[:-1]))
            currmap = []
    return seeds, maps


if __name__ == "__main__":
    seeds, maps = get_seeds_and_maps("input.txt")
    for m in maps:
        seeds = map(m, seeds)
    print(min(seeds))
