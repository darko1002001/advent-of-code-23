import re
from collections import defaultdict
from functools import reduce
from operator import mul


def solve(inputs) -> int:
    return sum([solve_input(input_) for input_ in inputs])


def solve_input(input_: str):
    dict_ = defaultdict(int)
    _, games_str = input_.split(":")
    games = games_str.split(";")
    for game in games:
        for tag in ["red", "green", "blue"]:
            count = extract_tag(game, tag)
            dict_[tag] = max(dict_[tag], count)
    return reduce(mul, dict_.values(), 1)


def extract_tag(game, tag):
    result = re.search(rf"(\d+)\s{tag}", game)
    return int(result.group(1)) if result else 0
