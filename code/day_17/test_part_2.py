from .part_2 import solve


def test_part_sample(load_text):
    lines = load_text("part_test")
    assert solve(lines) == 94


def test_part_sample_2(load_text):
    lines = load_text("part_test_2")
    assert solve(lines) == 71


def test_part(load_text):
    lines = load_text("part")
    assert solve(lines) == 993
