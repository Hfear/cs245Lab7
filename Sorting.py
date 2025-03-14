"""Generate a 10×10 matrix and sort by first column."""

import numpy as np

matrix = np.random.randint(0, 10, size=(10, 10))

print(matrix)
print(matrix[matrix[:, 0].argsort()])