import numpy as np
np.random.seed(42)
rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)  # Synthetic daily rainfall data
rainfall[np.random.choice(365, 100, replace=False)] = 0  # 100 dry days

"""Creating a Structured Array:
Create a structured NumPy array where each entry contains:
day (integer, 1 to 365)
rainfall (float, in mm)
is_rainy (Boolean, True if rainfall > 0)"""


# setting up structute of array using names aand types
# integer data type i4, float is f boolean is ?
structuredRainfall = np.dtype([('day','i4'),
         ('rainfall','f4'),
         ('is_rainy','?')])
# 365 days
structuredRainfall['day'] = np.arange(365)
#transferring over rainfall vals
structuredRainfall['rainfall'] = rainfall
# checking if try and storing the boolean
structuredRainfall['is_rainy'] = rainfall > 0

print(structuredRainfall)

"""Filtering Data with Structured Arrays:
Use Boolean masks on the structured array to extract all rainy days and compute their average rainfall.
"""



"""Sorting Structured Data:
Sort the structured array by rainfall and print the top 5 rainiest days."""