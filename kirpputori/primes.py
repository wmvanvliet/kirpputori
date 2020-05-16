"""
Functions relating to computing prime numbers.

Author: Marijn van Vliet <w.m.vanvliet@gmail.com>
"""


def first_n_primes(n):
    """Compute the first n prime numbers.

    Parameters
    ----------
    n : int
        Number of prime numbers to compute.

    Returns
    -------
    primes : list of int
        The first n prime numbers.

    Examples
    --------
    >>> first_n_primes(4)
    [1, 2, 3, 5]

    >>> first_n_primes(10)
    [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    """
    primes = []  # Prime numbers found so far
    candidate = 1  # Number to try for primeness

    while len(primes) < n:
        # See if the candidate number is prime
        for prime in primes:
            if candidate % prime == 0 and prime != 1:
                break  # Candidate is not prime!
        else:
            # No previous prime number was an equal divider of the candidate
            # number. This means the candidate is prime!
            primes.append(candidate)

        # Next iteration, try this candidate number:
        candidate += 1

    return primes
