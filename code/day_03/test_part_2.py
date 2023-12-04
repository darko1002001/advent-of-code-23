from .part_2 import solve


def test_part_sample(load_text):
    lines = load_text("part2_test")
    assert solve(lines) == 467835


def test_part(load_text):
    lines = load_text("part2")
    assert solve(lines) == 86879020