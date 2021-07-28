"""
Tests' fixtures
"""
from pytest import fixture

from divisiblelist import DivisibleList


@fixture
def sample_list():
    """Create a DivisibleList for tests."""

    return DivisibleList([i for i in range(72)])
