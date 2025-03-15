"""Extract every alternate row from a 5×5 matrix."""
import numpy as np

matrix = np.random.randint(0, 10, size=(5, 5))
print(matrix)

print(" \n alternate rows \n" , matrix[::2])