import re


def solve(inputs) -> int:
    sum = 0
    for input_ in inputs:
        sum += solve_input(input_)
    return sum


dict_ = {"red": 12, "green": 13, "blue": 14}
tags = ["red", "green", "blue"]


def solve_input(input: str):
    parts = input.split(":")
    id_ = int(parts[0][4:])
    games = parts[1].split(";")
    for game in games:
        for tag in tags:
            if dict_[tag] < extract_tag(game, tag):
                return 0
    return id_


def extract_tag(game, tag):
    pattern = re.compile(rf"(\d+)\s{tag}")
    result = pattern.search(game)
    if not result:
        return 0
    if item := result.group(1):
        return int(item)
    return 0
