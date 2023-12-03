import decimal


def is_dot(c):
    return c == "."


def is_special(c):
    return not c.isdigit() and not is_dot(c)


def check_around(inputs, r, c, num):
    to_print = []
    l = len(num)
    # print(f"checking {num=} {r=} {c=}")
    start_r = max(0, r - 1)
    end_r = min(len(inputs), r + 2)
    start_c = max(0, c - l - 1)
    end_c = min(c + 1, len(inputs[0]))
    # print(f"between {num=} {start_r=} {end_r=} {start_c=} {end_c=}")
    for current_r in range(start_r, end_r):
        to_print_r = ""
        for current_c in range(start_c, end_c):
            c_ = inputs[current_r][current_c]
            to_print_r += c_
            special = is_special(c_)
            # print(f"{special=} {current_r=} {current_c}")
            if special:
                return True
        to_print.append(to_print_r)
    print(f"{num=} not a part {to_print}")
    return False


def find_numbers(inputs: list[str]):
    items = []
    for r, row in enumerate(inputs):
        num = ""
        index = 0
        while index < len(row):
            c = row[index]
            if c.isdigit():
                num += c
            else:
                if num and check_around(inputs, r, index, num):
                    items.append(int(num))
                num = ""
            index += 1
        if num and check_around(inputs, r, index - 1, num):
            items.append(int(num))
    print(items)
    print(len(items))
    return items


def solve(inputs) -> int:
    numbers = find_numbers(inputs)
    return sum(numbers)
