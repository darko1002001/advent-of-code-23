from functools import cache


def read_input(input_):
    springs, ordering = input_.split(" ")
    groups = tuple(map(int, ordering.split(",")))  # as a list of numbers
    return "?".join([springs] * 5), groups * 5


@cache
def substitute(springs, groups) -> int:
    if not groups:
        return 1 if "#" not in springs else 0
    if len(springs) < sum(groups):
        return 0
    if springs[0] == ".":
        return substitute(springs[1:], groups)

    total = substitute(springs[1:], groups) if springs[0] == "?" else 0

    total += (
        substitute(springs[(groups[0] + 1) :], groups[1:])
        if all(s != "." for s in springs[: groups[0]])
        and (
            len(springs) > groups[0]
            and springs[groups[0]] != "#"
            or len(springs) <= groups[0]
        )
        else 0
    )
    return total


def solve(inputs) -> int:
    return sum([substitute(*read_input(input_)) for input_ in inputs])
