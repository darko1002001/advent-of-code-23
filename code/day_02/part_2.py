import re
from functools import reduce


def solve(inputs) -> int:
    return reduce(sum, [solve_input(input_) for input_ in inputs])


def solve_input(input_: str):
    dict_ = {"red": 0, "green": 0, "blue": 0}
    parts = input_.split(":")
    games = parts[1].split(";")
    for game in games:
        for tag in ["red", "green", "blue"]:
            count = extract_tag(game, tag)
            dict_[tag] = max(dict_[tag], count)
    return reduce(multiply, dict_.values(), 1)


def multiply(a, b):
    return a * b


def sum(a, b):
    return a + b


def extract_tag(game, tag):
    result = re.search(rf"(\d+)\s{tag}", game)
    if result and (item := result.group(1)):
        return int(item)
    return 0
