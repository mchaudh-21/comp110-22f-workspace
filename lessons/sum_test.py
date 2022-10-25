'''tests for sum fn.'''

from lessons.sum import sum

def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0

def test_sum_single_item() -> None:
    assert sum([110.0]) == 110.0

def test_sum_many_items() -> None:
    xs: list[float] = [1.0,2.0,3.0]
    assert sum(xs) == 6.0
