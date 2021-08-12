"""Test common behaviour for list divisions."""
from pytest import mark, raises

from .fixtures import sample_list  # noqa F401


class TestCommonPartDivibleList:
    """Test common behaviour for DivisibleList class for both division (/)
    and floor division (//)."""

    def test_if_raises_zero_division_error_for_division_by_zero(
        self, sample_list
    ) -> None:

        with raises(ZeroDivisionError):
            sample_list / 0
            sample_list // 0

    @mark.parametrize(
        "divisor", (True, {"1": 2}, 3.14159, [1, 2], (3, 4), "2")
    )
    def test_if_raises_type_error_for_any_type_not_supported(
        self, sample_list, divisor
    ) -> None:

        with raises(TypeError):
            sample_list / divisor
            sample_list // divisor

    def test_if_raises_value_error_for_division_by_negative_numbers(
        self, sample_list
    ) -> None:

        with raises(ValueError):
            sample_list / -1
            sample_list // -1
