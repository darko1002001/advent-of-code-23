import logging

from shapely import Polygon

logger = logging.getLogger(__name__)


def parse(line):
    d, steps, color = line.split(" ")
    return d, int(steps), color


directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}


def dig(instructions):
    points = [(0, 0)]
    total_steps = 0
    for d, steps, _ in instructions:
        rx, cx = directions[d]
        total_steps += steps
        r, c = points[-1]
        current = (r + rx * steps, c + cx * steps)
        points.append(current)
    return points, total_steps


def area(dig_site):
    # Shoelace Formula https://en.wikipedia.org/wiki/Shoelace_formula to calculate inner area
    # Pick's theorem https://en.wikipedia.org/wiki/Pick%27s_theorem to add the boundaries
    points, total_steps = dig_site
    p = Polygon(points)
    i = int(p.area) - total_steps // 2 + 1
    return i + total_steps


def solve(lines) -> int:
    instructions = [parse(line) for line in lines]
    dig_site = dig(instructions)
    return area(dig_site)
