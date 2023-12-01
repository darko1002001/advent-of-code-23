import re


def solve(inputs) -> int:
    sum = 0
    for input in inputs:
        sum += calculate_input(input)
    return sum


def calculate_input(input: str) -> int:
    result = re.sub("[^0-9]", "", input)
    return int(result[0] + "" + result[-1])
