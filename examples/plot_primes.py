"""
Visualize the first 100 prime numbers
=====================================

In this example, we will explore the first 100 prime numbers.

Author: Marijn van Vliet <w.m.vanvliet@gmail.com>
"""

# First we import the required modules.
from matplotlib import pyplot as plt
from kirpputori import first_n_primes

###############################################################################
# Now we can visualize the first 100 prime numbers using matplotlib.
plt.plot(first_n_primes(100))
