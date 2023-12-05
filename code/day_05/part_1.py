import re


def read_seeds(line):
    name, values = line.split(":")
    numbers = values.split()
    return [int(number) for number in numbers]


def find_ranges(inputs: list[str]):
    ranges = []
    start = 3
    index = 0
    for index in range(4, len(inputs)):
        if inputs[index].endswith("map:"):
            ranges.append((start, index - 2))
            start = index + 1
    ranges.append((start, index))
    return ranges


def make_interpolator(input_start, input_end, output_start):
    def interpolator(source):
        if source < input_start or source > input_end:
            return None
        diff = source - input_start
        result = output_start + diff
        return result

    return interpolator


def read_map(inputs, range_: tuple[int, int]):
    list_ = []
    pattern = re.compile(r"(\d+)")
    for index in range(range_[0], range_[1] + 1):
        input_ = inputs[index]
        numbers = [int(number.group(0)) for number in pattern.finditer(input_)]
        list_.append(numbers)

    interpolators = []
    for dest_range, source_range, range_length in list_:
        interpolators.append(
            make_interpolator(
                source_range,
                source_range + range_length - 1,
                dest_range,
            )
        )

    def mapper(source):
        for inter_ in interpolators:
            if value := inter_(source):
                return value
        return source

    return mapper


def mappings(dict_, inputs_) -> list[int]:
    return [dict_.get(input_, input_) for input_ in inputs_]


def solve(inputs) -> int:
    seeds = read_seeds(inputs[0])
    ranges = find_ranges(inputs)
    sources = seeds
    for mapper in (read_map(inputs, range_) for range_ in ranges):
        outputs = []
        for source in sources:
            outputs.append(mapper(source))
        sources = outputs
    return min(sources)
