import logging
from collections import defaultdict, deque, Counter
from functools import reduce
from operator import mul

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


def signal(devices, device_states):
    q = deque()
    q.append(("button", "broadcaster", False))
    pulses = {True: 0, False: 0}
    while q:
        source, name, pulse = q.popleft()
        pulses[pulse] += 1
        # logger.info(f"{source} -{pulse} -> {name}")
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
    return pulses


def solve(lines) -> int:
    state, dependencies = parse(lines)
    device_states = init_device_states(state, dependencies)
    cp = Counter({True: 0, False: 0})
    for count in range(1000):
        pulses = signal(state, device_states)
        cp.update(Counter(pulses))
    return reduce(mul, cp.values())
