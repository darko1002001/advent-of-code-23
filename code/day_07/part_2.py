def read_pair(item):
    hand, bet = item.split(" ")
    return hand, int(bet)


def score(hand: str):
    vals = [hand.count(card) for card in hand]
    if 5 in vals:
        return 6
    if 4 in vals:
        return 5
    if 3 in vals and 2 in vals:
        return 4
    if 3 in vals:
        return 3
    if vals.count(2) == 4:
        return 2
    if 2 in vals:
        return 1
    return 0


def make_variations(hand: str):
    if hand == "":
        return [""]
    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in make_variations(hand[1:])
    ]


def score_variations(hand: str):
    return max(map(score, make_variations(hand)))


mapping = {
    "T": "A",
    "J": "1",
    "Q": "C",
    "K": "D",
    "A": "E",
}


def rank(hand):
    ordered_ = str([mapping.get(h, h) for h in hand])
    score_ = score_variations(hand)
    return score_, ordered_


def solve(inputs) -> int:
    hand_pairs = [read_pair(input_) for input_ in inputs]
    hand_pairs.sort(key=lambda p: rank(p[0]))
    return sum([pair_[1] * index for index, pair_ in enumerate(hand_pairs, 1)])
