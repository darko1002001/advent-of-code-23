import re


def solve(inputs) -> int:
    sum = 0
    for input_ in inputs:
        sum += solve_input(input_)
    return sum


tags = ["red", "green", "blue"]


def solve_input(input: str):
    dict_ = {"red": 0, "green": 0, "blue": 0}
    parts = input.split(":")
    id_ = int(parts[0][4:])
    games = parts[1].split(";")
    for game in games:
        for tag in tags:
            count = extract_tag(game, tag)
            if dict_[tag] < count:
                dict_[tag] = count
    pow = 1
    for item in dict_.values():
        pow *= item
    return pow


def extract_tag(game, tag):
    pattern = re.compile(rf"(\d+)\s{tag}")
    result = pattern.search(game)
    if not result:
        return 0
    if item := result.group(1):
        return int(item)
    return 0
