"""File for testing utils functions."""
__author__ = "730550997"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


# tests for only_evens
def test_only_evens() -> None:
    """Tests edge case of empty list."""
    assert only_evens([]) == []


def test_only_evens_one() -> None:
    """Tests use case of all odd numbers."""
    list_odd = [1, 3, 5, 7]
    assert only_evens([list_odd]) == list_odd


def test_only_evens_two() -> None:
    """Tests use case of what a user input should output to."""
    user_input = [1, 2, 3, 4, 5]
    assert only_evens(user_input) == [2, 4]


# tests for concat
def test_concat() -> None:
    """Tests edge case of empty list."""
    assert concat([]) == []


def test_concat_one() -> None:
    """Tests use case of one empty list and a nonempty list."""
    assert concat([1, 2], []) == [1, 2]


def test_concat_two() -> None:
    """Test use case of possible user input and its output."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


# tests for sub
def test_sub() -> None:
    """Tests what happens if there is an empty lsit."""
    assert sub([], 1, 3) == []


def test_sub_one() -> None:
    """Tests use case of a negative start index."""
    example = [1, 2, 3, 4]
    assert sub(example, -2, 2) == [1, 2]


def test_sub_two() -> None:
    """Tests use case of out of range end index."""
    example = [1, 2, 3, 4]
    assert sub(example, 1, 9) == [2, 3, 4]