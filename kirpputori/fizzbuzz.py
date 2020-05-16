"""
Super advanced FizzBuzz algorithms.

Author: Marijn van Vliet <w.m.vanvliet@gmail.com>
"""


def fizzbuzz(end=100):
    """Generate a FizzBuzz game sequence.

    FizzBuzz is a childrens game where players take turns counting.
    The rules are as follows::

    1. Whenever the count is divisible by 3, the number is replaced with
       "Fizz"
    2. Whenever the count is divisible by 5, the number is replaced with "Buzz"
    3. Whenever the count is divisible by both 3 and 5, the number is replaced
       with "FizzBuzz"

    Parameters
    ----------
    end : int
        The FizzBuzz sequence is generated up and including this number.

    Returns
    -------
    sequence : list of str
        The FizzBuzz sequence.

    Examples
    --------
    >>> fizzbuzz(3)
    ['1', '2', 'Fizz']

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    References
    ----------
    https://blog.codinghorror.com/why-cant-programmers-program/
    """
    sequence = []
    for i in range(1, end + 1):
        if i % (3 * 5) == 0:
            sequence.append('FizzBuzz')
        elif i % 3 == 0:
            sequence.append('Fizz')
        elif i % 5 == 0:
            sequence.append('Buzz')
        else:
            sequence.append(str(i))
    return sequence
