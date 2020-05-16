from kirpputori import first_n_primes


def test_first_n_primes():
    """Test generating prime numbers."""
    assert first_n_primes(0) == []
    assert first_n_primes(1) == [1]
    assert first_n_primes(4) == [1, 2, 3, 5]
    assert first_n_primes(10) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
