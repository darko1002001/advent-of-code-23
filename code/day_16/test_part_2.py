from .part_2 import solve


def test_part_sample(load_text):
    lines = load_text("part_test")
    assert solve(lines) == 51


def test_part(load_text):
    lines = load_text("part")
    assert solve(lines) == 9064
