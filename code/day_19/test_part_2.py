from .part_2 import solve


def test_part_sample(load_sections):
    lines = load_sections("part_test")
    assert solve(lines) == 167409079868000


def test_part(load_sections):
    lines = load_sections("part")
    assert solve(lines) == 121158073425385
