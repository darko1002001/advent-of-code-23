def solve_row(input_) -> int:
    if input_.count(0) == len(input_):
        return 0
    result = [y - x for x, y in zip(input_[:-1], input_[1:])]
    return solve_row(result) + input_[-1]


def solve(inputs) -> int:
    return sum([solve_row(list(map(int, input_.split()))) for input_ in inputs])
