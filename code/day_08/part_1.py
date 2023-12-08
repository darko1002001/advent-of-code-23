def parse(inputs):
    instructions = inputs[0]
    return instructions, (
        {input_[0:3]: (input_[7:10], input_[12:15]) for input_ in inputs[2:]}
    )


def solve(inputs) -> int:
    instructions, rows = parse(inputs)
    index = 0
    current = "AAA"
    while True:
        next_ = instructions[index % len(instructions)]
        index += 1
        # print(f"{current} {rows[current]=}")
        current = rows[current][1 if next_ == "R" else 0]
        if current == "ZZZ":
            return index
