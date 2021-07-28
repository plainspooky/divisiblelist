from pytest import mark, raises

from .fixtures import sample_list

class TestChunkDivisionForDivisibleList:
    """Test specific cases for chunk division."""

    @mark.parametrize("divisor", (True, 3.14159, [1, 2], (3, 4), "2"))
    def test_if_ignores_a_set_with_anything_but_a_integer(self, sample_list, divisor) -> None:
        with raises(TypeError):
            assert sample_list / {divisor}

    @mark.parametrize("divisor", (1, 2, 3, 4, 6, 8, 9, 12, 24, 72))
    def test_if_returns_lists_cointaining_divided_in_an_equal_number_of_elements(
        self, sample_list, divisor
    ) -> None:

        expected_size = len(sample_list) // divisor
        result = [len(i) for i in sample_list / {divisor}]
        print(expected_size, divisor, sample_list, result)
        assert divisor in result
