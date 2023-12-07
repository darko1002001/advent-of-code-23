from collections import defaultdict


def read_pair(item):
    hand, bet = item.split(" ")
    return hand, int(bet)


def score(dict_: dict[str, int]):
    vals = dict_.values()
    if 5 in vals:
        return 6
    if 4 in vals:
        return 5
    if 3 in vals and 2 in vals:
        return 4
    if 3 in vals:
        return 3
    if list(vals).count(2) == 2:
        return 2
    if 2 in vals:
        return 1
    return 0


mapping = {
    "T": "A",
    "J": "B",
    "Q": "C",
    "K": "D",
    "A": "E",
}


def rank(hand):
    dict_ = defaultdict(int)
    ordered_ = ""
    for h in hand:
        dict_[h] += 1
        ordered_ += mapping.get(h, h)

    score_ = score(dict_)
    print(f"{hand=} {dict_} {score_} {ordered_}")
    return score_, ordered_


def solve(inputs) -> int:
    hand_pairs = [read_pair(input_) for input_ in inputs]
    mapped_pairs = [(*rank(hand[0]), hand[1]) for hand in hand_pairs]
    print(mapped_pairs)
    sorted_pairs = list(sorted(mapped_pairs, key=lambda x: (x[0], x[1])))
    return sum([pair_[2] * (index + 1) for index, pair_ in enumerate(sorted_pairs)])
