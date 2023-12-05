def read_seeds(line):
    _, values = line.split(":")
    return list(map(int, values.split()))


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


def read_map(inputs, range_: tuple[int, int]):
    list_ = []
    for index in range(range_[0], range_[1] + 1):
        input_ = inputs[index]
        numbers = list(map(int, input_.split()))
        list_.append(numbers)
    return list_


def find_maps(inputs):
    ranges = find_ranges(inputs)
    return [read_map(inputs, range_) for range_ in ranges]


def solve(inputs) -> int:
    seeds = read_seeds(inputs[0])
    seeds = [
        (seeds[index], seeds[index] + seeds[index + 1])
        for index in range(0, len(seeds), 2)
    ]
    maps = find_maps(inputs)

    # We keep breaking down the seeds into smaller ranges until we can map every range
    for map_ in maps:
        new_seeds = []
        while seeds:
            start, end = seeds.pop()
            for dest_range_start, source_range_start, range_length in map_:
                source_range_end = source_range_start + range_length
                overlap_start = max(start, source_range_start)
                overlap_end = min(end, source_range_end)
                if overlap_start < overlap_end:  # has overlap
                    # add the overlapping region as seeds
                    new_seeds.append(
                        (
                            overlap_start - source_range_start + dest_range_start,
                            overlap_end - source_range_start + dest_range_start,
                        )
                    )
                    # add region to process in next row from same map when before region exists
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    # add region to process in next row from same map when after region exists
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    # this seed is handled we can move on to the next one
                    break
            else:
                # there is no mapping for the seed in the whole map, so add as is and move to next map
                new_seeds.append((start, end))
        seeds = new_seeds

    return min(seeds)[0]
