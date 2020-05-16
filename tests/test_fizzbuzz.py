from kirpputori import fizzbuzz


def test_fizzbuzz():
    """Test the FizzBuzz function."""
    assert fizzbuzz(0) == []
    assert fizzbuzz(1) == ['1']
    assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']
    assert fizzbuzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8',
                            'Fizz', 'Buzz', '11', 'Fizz', '13', '14',
                            'FizzBuzz']
