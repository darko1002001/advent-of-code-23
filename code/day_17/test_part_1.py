from .part_1 import solve


def test_part_1_sample(load_text):
    lines = load_text("part_test")
    assert solve(lines) == 102


def test_part_1(load_text):
    lines = load_text("part")
    assert solve(lines) == 845
