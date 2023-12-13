from .part_2 import solve


def test_part_sample(load_sections):
    sections = load_sections("part2_test")
    assert solve(sections) == 400


def test_part(load_sections):
    sections = load_sections("part2")
    assert solve(sections) == 28806
