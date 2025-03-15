"""You are provided with an array representing daily rainfall (in mm) over a year in a fictional city:
"""
import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)  # Synthetic daily rainfall data

rainfall[np.random.choice(365, 100, replace=False)] = 0  # 100 dry days

"""Basic Rainy Day Count:
Use a Boolean mask to find how many days had rain (i.e., rainfall > 0 mm)."""

basicRainMask = rainfall > 0
RainyDayCount = np.sum(basicRainMask)

print("Rainy Day count : ", RainyDayCount)

"""Heavy Rain Days:
Find the percentage of days where rainfall exceeded 5 mm."""
heavyRainDays = RainyDayCount > 5
percentHeavyRainDays = (np.sum(heavyRainDays) / 365) * 100

print("percentage heavy rain : ", percentHeavyRainDays)

"""Dry Spells:
Find the longest consecutive sequence of dry days (rainfall == 0)."""

dryDayMask = rainfall == 0

longestConsecutiveDryDays = 0
currentstreak= 0

for i in range(365):
    if dryDayMask[i]:
        currentstreak += 1
        longestConsecutiveDryDays = max(longestConsecutiveDryDays, currentstreak)
    else:
        currentstreak = 0

print("longest dry days : ", longestConsecutiveDryDays)
