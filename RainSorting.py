import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)  # Synthetic daily rainfall data

rainfall[np.random.choice(365, 100, replace=False)] = 0  # 100 dry days

"""Sorting Rainfall Data:
Sort the rainfall array in ascending order and find the median rainfall value.
"""

sortedRainfall = np.sort(rainfall)
medianRainfall = np.median(sortedRainfall)
print("median rainfall:", medianRainfall.round(2))

"""Percentile Analysis:
Find the 90th percentile of rainfall (i.e., the rainfall value above which only 10% of days occur)."""

ninteyPercentile = np.percentile(sortedRainfall, 90)
print("90th percentile:", ninteyPercentile.round(2))