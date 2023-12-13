import logging

logger = logging.getLogger(__name__)


def almost_same(s1, s2):
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff += 1
    return diff == 1


def check_index(section, index):
    current = 0
    smudge_changed = False
    while index - current - 1 >= 0 and index + current < len(section):
        s1 = section[index - current - 1]
        s2 = section[index + current]
        if s1 != s2:
            if smudge_changed:
                return False
            if almost_same(s1, s2):
                smudge_changed = True
            else:
                return False
        current += 1
    return smudge_changed


def reflect(section):
    for index in range(1, len(section)):
        if check_index(section, index):
            return index
    return None


def transpose(section):
    transposed = list(map("".join, zip(*section)))
    return transposed


def solve(sections) -> int:
    logger.info("Hello")
    rows = 0
    cols = 0
    for section in sections:
        if row_count := reflect(section):
            rows += row_count
        if col_count := reflect(transpose(section)):
            cols += col_count
    return cols + 100 * rows
