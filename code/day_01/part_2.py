def solve(inputs) -> int:
    return sum((calculate_input(input_) for input_ in inputs))


items = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def calculate_input(input: str) -> int:
    res_str = ""

    for i in range(0, len(input)):
        c = input[i]
        if c.isdigit():
            res_str += c
        else:
            substr = input[i:]
            for i2 in range(0, len(items)):
                item = items[i2]
                if substr.startswith(item):
                    res_str += str(i2 + 1)

    return int(res_str[0] + "" + res_str[-1])
