import numpy as np


def pythagoras(a, b):
    """Compute pythagoras.

    Parameters
    ----------
    a : float
        length of one side of the triangle
    b : float
        length of second side

    Returns
    -------
    c : float
        length of the hypothenuse
    """
    return np.sqrt(a**2 + b**2)
