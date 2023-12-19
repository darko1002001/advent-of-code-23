import logging
import re

logger = logging.getLogger(__name__)


def parse_parts(parts):
    return [
        tuple(segment.split("=")[1] for segment in part[1:-1].split(","))
        for part in parts
    ]


def parse_workflows(workflows):
    items = {}
    for workflow in workflows:
        name, conditions = workflow.split("{")
        conditions = conditions[:-1]
        conditions = conditions.split(",")
        final_outcome = conditions[-1]
        conditions = conditions[:-1]
        conditions = [tuple(item.split(":")) for item in conditions]
        items[name] = (conditions, final_outcome)
    items["A"] = ["A"]
    items["R"] = ["R"]
    return items


accepted = []

prop_map = {"x": 0, "m": 1, "a": 2, "s": 3}


def process(part, workflow, workflows):
    if workflow == ["A"]:
        accepted.append(part)
        return
    if workflow == ["R"]:
        return

    for step in workflow[0]:
        condition, next_ = step
        prop, value = re.split(r"[<>]", condition)
        value = int(value)
        resolved = int(part[prop_map[prop]])
        if "<" in condition:
            if resolved < value:
                return process(part, workflows[next_], workflows)
        elif ">" in condition:
            if resolved > value:
                return process(part, workflows[next_], workflows)
    return process(part, workflows[workflow[1]], workflows)


def solve(inputs) -> int:
    workflows = parse_workflows(inputs[0])
    parts = parse_parts(inputs[1])
    start = workflows["in"]
    for part in parts:
        process(part, start, workflows)
    return sum([sum([int(i) for a in accepted for i in a])])
