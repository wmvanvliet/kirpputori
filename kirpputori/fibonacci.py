def fibonacci(length=10):
    """Get fibonacci sequence given it length.

    Parameters
    ----------
    length : int
        The length of the desired sequence.

    Returns
    -------
    sequence : list of int
        The desired Fibonacci sequence
    """
    if length < 1:
        raise ValueError("Sequence length must be > 0")

    sequence = [0] * (length + 2)
    sequence[0] = 0
    sequence[1] = 1
    for i in range(2, len(sequence)):
        sequence[i] = sequence[i - 1] + sequence[i - 2]
    return sequence[: -2]
