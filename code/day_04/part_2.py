import re
from collections import defaultdict


def solve(inputs) -> int:
    dict_ = dict(read_card(card) for card in inputs)
    totals = defaultdict(int)
    for index in range(1, len(inputs) + 1):
        winnings = dict_[index]
        copies = totals[index]
        totals[index] += 1
        for next_ in range(index + 1, index + winnings + 1):
            totals[next_] += copies + 1
    return sum(totals.values())


def read_card(input_: str):
    name, numbers = input_.split(":")
    winning, current = numbers.split(" | ")
    pattern = re.compile(r"(\d+)")
    id_ = int(pattern.search(name).group(0))
    winning_numbers = [match.group(0) for match in pattern.finditer(winning)]
    current_numbers = [match.group(0) for match in pattern.finditer(current)]
    won_count = sum([1 if num in winning_numbers else 0 for num in current_numbers])
    return id_, won_count
