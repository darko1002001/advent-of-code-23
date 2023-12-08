from itertools import count
from math import gcd


def parse(inputs):
    instructions = inputs[0]
    return instructions, (
        {input_[0:3]: (input_[7:10], input_[12:15]) for input_ in inputs[2:]}
    )


def find_step_count(current, instructions, rows):
    for index in count(start=0, step=1):
        next_ = instructions[index % len(instructions)]
        position = 1 if next_ == "R" else 0
        current = rows[current][position]
        if current.endswith("Z"):
            return index + 1


def calculate(steps) -> int:
    current = steps.pop()
    while steps:
        next_step = steps.pop()
        current = current * next_step // gcd(current, next_step)
    return current


def solve(inputs) -> int:
    instructions, rows = parse(inputs)
    current_items = set(filter(lambda k: k.endswith("A"), rows.keys()))
    steps = [find_step_count(current, instructions, rows) for current in current_items]
    return calculate(steps)
