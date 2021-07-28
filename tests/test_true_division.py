from pytest import mark, raises

from .fixtures import sample_list

class TestDivisionForDivisibleList:
    """Test specific behavior for common division ("/")."""

    @mark.parametrize("divisor", (1, 2, 3, 4, 6, 8, 9, 12, 24, 72))
    def test_if_returns_the_list_divided_in_an_equal_number_of_elements(
        self, sample_list, divisor
    ) -> None:

        expected_size = len(sample_list) / divisor

        assert expected_size in [len(i) for i in sample_list / divisor]

    @mark.parametrize("divisor", (5, 7, 10, 11, 48))
    def test_if_raises_value_error_if_dividend_and_divisor_arent_multiples(
        self, sample_list, divisor
    ) -> None:

        with raises(ValueError):
            sample_list / divisor
