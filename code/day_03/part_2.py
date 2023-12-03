import operator
from collections import defaultdict
from functools import reduce


def is_dot(c):
    return c == "."


def is_star(c):
    return c == "*"


def is_special(c):
    return not c.isdigit() and not is_dot(c)


def check_around(inputs, r, c, num):
    num_len = len(num)
    start_r = max(0, r - 1)
    end_r = min(len(inputs), r + 2)
    start_c = max(0, c - num_len - 1)
    end_c = min(c + 1, len(inputs[0]))
    for current_r in range(start_r, end_r):
        for current_c in range(start_c, end_c):
            c_ = inputs[current_r][current_c]
            if is_special(c_) and is_star(c_):
                return current_r, current_c
    return None


def find_numbers(inputs: list[str]):
    items = []
    for r, row in enumerate(inputs):
        num = ""
        for index, c in enumerate(row):
            if c.isdigit():
                num += c
            if not c.isdigit() or index == len(row) - 1:
                if num and (index_ := check_around(inputs, r, index, num)):
                    items.append((int(num), index_))
                num = ""

    print(items)
    return items


def solve(inputs) -> int:
    numbers = find_numbers(inputs)
    groups = defaultdict(list)
    for number in numbers:
        groups[number[1]].append(number[0])
    return sum(
        [
            reduce(operator.mul, group, 1) if len(group) == 2 else 0
            for group in groups.values()
        ]
    )
