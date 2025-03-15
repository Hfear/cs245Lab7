"""Generate 100 random numbers,
find numbers divisible by 3,
and replace them with -1."""

import numpy as np

randnums = np.random.randint(100, size=100)

print(randnums)

randnums[randnums % 3 == 0] = -1

print(randnums)