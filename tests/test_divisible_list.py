from pytest import fixture, mark, raises

from divisiblelist import DivisibleList


@fixture
def sample_list():
    """Create a DivisibleList for tests."""

    return DivisibleList([i for i in range(72)])


class TestDivibleList:
    """Test for DivisibleList class."""

    def test_if_raises_zero_division_error_for_division_by_zero(
        self, sample_list
    ) -> None:

        with raises(ZeroDivisionError):
            sample_list / 0

    @mark.parametrize("value", (False, {1: 2}, 3.14159, [1, 2], (3, 4), "2"))
    def test_if_raises_type_error_for_any_type_but_integers(
        self, sample_list, value
    ) -> None:

        with raises(TypeError):
            sample_list / value

    def test_if_raises_value_error_for_division_by_negative_numbers(
        self, sample_list
    ) -> None:

        with raises(ValueError):
            sample_list / -1

    @mark.parametrize("divisor", (1, 2, 3, 4, 6, 8, 9, 12, 24, 72))
    def test_if_returns_the_list_divided_in_an_equal_number_of_elements(
        self, sample_list, divisor
    ) -> None:

        expected_size = len(sample_list) // divisor

        assert expected_size in [len(i) for i in sample_list / divisor]

    @mark.parametrize("divisor", (5, 7, 10, 11, 48))
    def test_if_raises_value_error_if_dividend_and_divisor_arent_multiples(
        self, sample_list, divisor
    ) -> None:

        with raises(ValueError):
            sample_list / divisor
