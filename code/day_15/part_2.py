import logging
import re

logger = logging.getLogger(__name__)


def parse(lines):
    command = lines[0].split(",")
    pattern = r"(\w+)(=|-)(\d+)?"
    return [re.search(pattern, command).groups() for command in command]


def hash(code):
    val = 0
    for ch in code:
        val = ((val + ord(ch)) * 17) % 256
    return val


def calculate(boxes, code):
    label, sign, val = code
    h = hash(label)
    box = boxes[h]
    if sign == "=":
        found_index = next(
            (index for index, item in enumerate(box) if item[0] == label), -1
        )
        if found_index >= 0:
            box[found_index] = (label, val)
        else:
            box.append((label, val))
    elif sign == "-":
        box = [item for item in box if item[0] != label]
    boxes[h] = box


def solve(inputs) -> int:
    codes = parse(inputs)
    boxes = [[] for _ in range(256)]

    for code in codes:
        calculate(boxes, code)

    return sum(
        [
            (1 + index) * (item_index + 1) * int(item[1])
            for index, box in enumerate(boxes)
            for item_index, item in enumerate(box)
        ]
    )
