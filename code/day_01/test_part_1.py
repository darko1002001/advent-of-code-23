from .part_1 import solve


def test_part(load_text):
    lines = load_text("part1")
    print(lines)
    assert solve() is None
