from functools import reduce
from operator import mul


def read(inputs) -> tuple[int, int]:
    time = list(map(int, inputs[0].split(":")[1].split()))
    distance = list(map(int, inputs[1].split(":")[1].split()))
    return tuple(zip(time, distance))


def find_winning(record):
    time, distance = record
    ways = 0
    for hold_time in range(0, time + 1):
        if did_win(hold_time, time, distance):
            ways += 1
    return ways


def did_win(hold_time, total_time, distance_to_beat):
    travel_distance = (total_time - hold_time) * hold_time
    return travel_distance > distance_to_beat


def solve(inputs) -> int:
    records = read(inputs)
    return reduce(mul, [find_winning(record) for record in records], 1)
