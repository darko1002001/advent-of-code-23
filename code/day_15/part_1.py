import logging

logger = logging.getLogger(__name__)


def parse(lines):
    return lines[0].split(",")


def hash(code):
    val = 0
    for ch in code:
        val = ((val + ord(ch)) * 17) % 256
    return val


def solve(inputs) -> int:
    codes = parse(inputs)
    return sum(hash(code) for code in codes)
