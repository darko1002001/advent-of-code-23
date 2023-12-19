from .part_1 import solve


def test_part_1_sample(load_sections):
    lines = load_sections("part_test")
    assert solve(lines) == 19114


def test_part_1(load_sections):
    lines = load_sections("part")
    assert solve(lines) == 348378
