import re


def solve(inputs) -> int:
    return sum([read_card(card) for card in inputs])


def read_card(input_: str):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    name, numbers = input_.split(":")
    winning, current = numbers.split(" | ")
    pattern = re.compile(r"(\d+)")
    winning_numbers = [match.group(0) for match in pattern.finditer(winning)]
    current_numbers = [match.group(0) for match in pattern.finditer(current)]
    common_numbers = set(winning_numbers).intersection(current_numbers)
    won_count = len(common_numbers)
    return 1 << won_count - 1 if won_count > 0 else 0
