def check_index(section, index):
    current = 0
    while index - current - 1 >= 0 and index + current < len(section):
        if section[index - current - 1] != section[index + current]:
            return False
        current += 1
    return True


def reflect(section):
    for index in range(1, len(section)):
        if check_index(section, index):
            return index
    return None


def transpose(section):
    transposed = list(map("".join, zip(*section)))
    return transposed


def solve(sections) -> int:
    rows = 0
    cols = 0
    for section in sections:
        if row_count := reflect(section):
            rows += row_count
        elif col_count := reflect(transpose(section)):
            cols += col_count
    return cols + 100 * rows
