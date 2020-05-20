from kirpputori.pythagoras import pythagoras
import numpy


def test_pythagoras():
    """Test the pythagoras function."""
    assert pythagoras(0, 0) == 0
    assert pythagoras(1, 1) == numpy.sqrt(2)
