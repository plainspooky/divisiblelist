"""Test chunk division."""
from pytest import mark, raises

from .fixtures import sample_list  # noqa F401


class TestChunkDivisionForDivisibleList:
    """Test specific cases for chunk division. (List split in a specific
    number of elements.)"""

    @mark.parametrize("divisor", (True, 3.14159, [1, 2], (3, 4), "2"))
    def test_if_ignores_content_inside_set_with_everything_but_an_integer(
        self, sample_list, divisor
    ) -> None:

        with raises(TypeError):
            assert sample_list / {divisor}

    @mark.parametrize("divisor", (1, 2, 3, 4, 6, 8, 9, 12, 24, 72))
    def test_if_returns_lists_cointaining_the_requested_number_of_items(
        self, sample_list, divisor
    ) -> None:

        expected_size = len(sample_list) // divisor
        result = [len(i) for i in sample_list / {divisor}]
        print(expected_size, divisor, sample_list, result)

        assert divisor in result
