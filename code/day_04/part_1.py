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
    won_count = sum([1 if num in winning_numbers else 0 for num in current_numbers])
    if won_count == 0:
        return 0
    score = 1
    for count in range(0, won_count - 1):
        score *= 2
    return score
