from .part_2 import solve


def test_part(load_text):
    lines = load_text("part")
    assert solve(lines) == 241528477694627
