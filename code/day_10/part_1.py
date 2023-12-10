def find_start(inputs):
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            if inputs[i][j] == "S":
                return (i, j)


# J F L 7 | - .
def is_connected(char, from_direction):
    if from_direction == "T":
        if char == "J":
            return "L"
        if char == "|":
            return "B"
        if char == "L":
            return "R"
    if from_direction == "L":
        if char == "J":
            return "T"
        if char == "-":
            return "R"
        if char == "7":
            return "B"
    if from_direction == "R":
        if char == "L":
            return "T"
        if char == "-":
            return "L"
        if char == "F":
            return "B"
    if from_direction == "B":
        if char == "|":
            return "T"
        if char == "F":
            return "R"
        if char == "7":
            return "L"
    return None


directions = [(0, 1, "L"), (0, -1, "R"), (1, 0, "T"), (-1, 0, "B")]
directions_map = {
    "L": (0, -1),
    "R": (0, 1),
    "T": (-1, 0),
    "B": (1, 0),
}

opposite_directions = {"R": "L", "L": "R", "B": "T", "T": "B"}


def move(inputs, current, direction):
    diff = directions_map[direction]
    x, y = current[0] + diff[0], current[1] + diff[1]
    opposite = opposite_directions[direction]
    if connection := is_connected(inputs[x][y], opposite):
        return (x, y), connection
    return None


def solve(inputs) -> int:
    start = find_start(inputs)
    movements = [move(inputs, start, d) for d in directions_map]
    a, b = [m for m in movements if m is not None]
    step = 2
    while True:
        a = move(inputs, a[0], a[1])
        b = move(inputs, b[0], b[1])
        if a[0] == b[0]:
            return step
        step += 1
