from functools import cache


def read_input(input_):
    springs, groups = input_.split(" ")
    mapped_groups = tuple(map(int, groups.split(",")))  # as a list of numbers
    return springs, mapped_groups


@cache
def substitute(springs, groups) -> int:
    if not groups:
        return 1 if "#" not in springs else 0
    if len(springs) < sum(groups):
        return 0
    if springs[0] == ".":
        return substitute(springs[1:], groups)

    total = 0
    if springs[0] == "?":
        total += substitute(springs[1:], groups)

    if (
        "." not in springs[: groups[0]]
        and len(springs) > groups[0]
        and springs[groups[0]] != "#"
        or len(springs) <= groups[0]
    ):
        total += substitute(springs[(groups[0] + 1) :], groups[1:])
    return total


def solve(inputs) -> int:
    return sum([substitute(*read_input(input_)) for input_ in inputs])
