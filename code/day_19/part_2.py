import logging
import re
from functools import reduce
from operator import mul

logger = logging.getLogger(__name__)


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
    return items


def process(part, name, workflows) -> int:
    if name == "R":
        return 0
    if name == "A":
        return reduce(mul, [(max_ - min_ + 1) for min_, max_ in part.values()])

    total = 0
    steps, fallback = workflows[name]
    for step in steps:
        condition, next_workflow_name = step
        condition_property, condition_value = re.split(r"[<>]", condition)
        condition_value = int(condition_value)
        min_, max_ = part[condition_property]

        if "<" in condition:
            interval_in = (min_, condition_value - 1)
            interval_out = (condition_value, max_)
        else:
            interval_in = (condition_value + 1, max_)
            interval_out = (min_, condition_value)

        if interval_in[0] <= interval_in[1]:  # valid range
            new_part = dict(part)
            new_part[condition_property] = interval_in
            total += process(new_part, next_workflow_name, workflows)
        if interval_out[0] <= interval_out[1]:  # valid range
            # there is a part to process in the next step or default fallback
            part = dict(part)
            part[condition_property] = interval_out
        else:
            part = None
            break  # no valid part remains to process by next conditions so break out
    if part:
        # there is a valid part left we can process with the default fallback
        total += process(part, fallback, workflows)
    return total


def solve(inputs) -> int:
    workflows = parse_workflows(inputs[0])
    part = {key: (1, 4000) for key in "xmas"}
    return process(part, "in", workflows)
