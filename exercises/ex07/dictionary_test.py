"""Test file for dictionary file."""
__author__ = "730550997"

import pytest

from exercises.ex07.dictionary import invert


def test_invert() -> None:
    """Test that takes care of empty dictionary."""
    assert invert({}) == {}


def test_invert_one() -> None:
    """Tests use case."""
    with pytest.raises(KeyError):
        dict1 = {"kris":"jordon","michael":"jordon"}
        invert(dict1)


def test_invert_two() -> None:
    """Test use case two, what user input shoudl output to."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


from exercises.ex07.dictionary import favorite_color


def test_favorite_color() -> None:
    """Function that takes care of empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_two() -> None:
    """Test function that gives correct output based on input."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_two() -> None:
    """Test function, if the input dictionary has integers instead of strings."""
    assert favorite_color({1:"blue", 2:"blue", 3:"green"}) == TypeError


from exercises.ex07.dictionary import count


def test_count() -> None:
    """Tests empty input."""
    assert count([]) == {}


def test_count_one() -> None:
    """Tests if list input has wrong value types."""
    assert count([1,2,3,3]) == TypeError


def test_count_two() -> None:
    """Tests the correct answer based on user input."""
    assert count(["a","a","b"]) == {"a":2, "b":1}
    