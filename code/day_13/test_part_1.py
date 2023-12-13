from .part_1 import solve


def test_part_1_sample(load_sections):
    sections = load_sections("part1_test")
    assert solve(sections) == 405


def test_part_1(load_sections):
    sections = load_sections("part1")
    assert solve(sections) == 33047
