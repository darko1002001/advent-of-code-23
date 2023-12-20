import logging
from collections import defaultdict, deque
from functools import reduce
from math import lcm

logger = logging.getLogger(__name__)


def parse(lines: list[str]):
    state = defaultdict(lambda: ("", []))
    dependencies = defaultdict(list)
    for line in lines:
        name, targets = line.split(" -> ")
        targets = tuple(targets.split(", "))
        type_ = ""
        if name[0] in "%&":
            type_ = name[0]
            name = name[1:]
        for t in targets:
            dependencies[t].append(name)
        state[name] = (type_, targets)

    return state, dependencies


def init_device_states(state, dependencies):
    current_states = {}
    for key, value in state.items():
        if value[0] == "%":
            current_states[key] = False
        elif value[0] == "&":
            current_states[key] = {d: False for d in dependencies[key]}
    return current_states


def signal(devices, device_states, level_1, level_2):
    q = deque()
    count = 0
    level_2_cycles = {}
    seen = {key: 0 for key in level_2}
    while True:
        count += 1
        q.append(("button", "broadcaster", False))
        while q:
            source, name, pulse = q.popleft()
            # When our Level 1 Conjunction module receives a True then we mark it. this source will cycle (emit True each X counts)
            # When all Level 2 sources sources cycle at least once with a True value we can use the lowest
            # common multiplier of the counts of each to see when False will be emitted from Level 1 to our target RX module
            if name == level_1 and pulse:
                seen[source] += 1

                if source not in level_2_cycles:
                    level_2_cycles[source] = count

                if all(seen.values()):
                    return reduce(lcm, level_2_cycles.values(), 1)

            type_, targets = devices[name]
            if type_ == "":
                for t in targets:
                    q.append((name, t, pulse))
            elif type_ == "%":
                if not pulse:
                    new_state = not device_states[name]
                    device_states[name] = new_state
                    for t in targets:
                        q.append((name, t, new_state))
            else:
                state = device_states[name]
                state[source] = pulse
                new_state = not all(state.values())
                for t in targets:
                    q.append((name, t, new_state))
    return False


def trim(state, dependencies):
    related = dependencies["rx"]
    return related[0], dependencies[related[0]]


def solve(lines) -> int:
    state, dependencies = parse(lines)
    # Level 1 is the device that outputs to RX. it is only one such device
    # Level 2 is a list of devices that output to the Level 1 device
    # Those devices are all Conjunction modules
    level_1, level_2 = trim(state, dependencies)
    device_states = init_device_states(state, dependencies)
    logger.info(f"{level_1=}")
    logger.info(f"{level_2=}")

    return signal(state, device_states, level_1, level_2)
