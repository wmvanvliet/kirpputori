from pytest import raises
from kirpputori.fibonacci import fibonacci


def test_fibonacci():
    """Test generating fibonacci sequences."""
    assert fibonacci() == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    with raises(ValueError, match="Sequence length must be > 0"):
        fibonacci(-1)
