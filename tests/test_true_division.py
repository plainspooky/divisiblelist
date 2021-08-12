"""Tests for list division."""
from pytest import mark

from .fixtures import sample_list  # noqa F401


class TestDivisionForDivisibleList:
    """Test specific behavior for common division ("/")."""

    @mark.parametrize("divisor", (1, 2, 3, 5, 7, 9, 11, 13, 17, 19, 72))
    def test_if_divided_list_contains_at_least_one_list_with_expected_length(
        self, sample_list, divisor
    ) -> None:

        expected_size = len(sample_list) // divisor

        assert expected_size in [len(i) for i in sample_list / divisor]
