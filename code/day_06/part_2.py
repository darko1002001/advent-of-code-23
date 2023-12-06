def read(inputs) -> tuple[int, int]:
    time = int(inputs[0].split(":")[1].replace(" ", ""))
    distance = int(inputs[1].split(":")[1].replace(" ", ""))
    return time, distance


def find_winning(record):
    time, distance = record
    left_range = binary_search_left(record)
    print(left_range)
    right_range = binary_search_right(record)
    print(left_range, right_range)
    return right_range - left_range + 1


def binary_search_left(record):
    time, distance = record
    start = 0
    end = time
    while start < end:
        mid = (start + end) // 2
        if did_win(mid, time, distance):
            end = mid
        else:
            start = mid + 1
    return start


def binary_search_right(record):
    time, distance = record
    start = 0
    end = time
    while start < end:
        mid = (start + end) // 2
        if did_win(mid, time, distance):
            start = mid + 1
        else:
            end = mid - 1
    return start


def did_win(hold_time, total_time, distance_to_beat):
    travel_distance = (total_time - hold_time) * hold_time
    return travel_distance > distance_to_beat


def solve(inputs) -> int:
    record = read(inputs)
    return find_winning(record)
