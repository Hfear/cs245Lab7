import numpy as np

np.random.seed(42)

rainfall = np.random.gamma(shape=2.0, scale=2.0, size=365)  # Synthetic daily rainfall data

rainfall[np.random.choice(365, 100, replace=False)] = 0  # 100 dry days

"""Top Rainfall Days:
Find the 10 wettest days of the year using fancy indexing."""

rainMask = rainfall > 0

#all the dates that rained
rainDates = np.where(rainMask)[0]

# the values corresponding with those dates
rainVals = rainfall[rainDates]

# indicies of rain values when sorted descending
#arg sort, returns array sorts by acending value
#and STORES by its index!!! oHHHHHH
indexSorted = np.flip(np.argsort(rainVals))

#cut down the array to only top 10
tenWettestIndexes =  indexSorted[:10]

#mapping index to actual dates
wettestDates = rainDates[tenWettestIndexes]
wettestVals = rainVals[tenWettestIndexes]

for i in range(10):
    print(i+1 ,". date: ", wettestDates[i], " value: ", wettestVals[i].round(2))

"""Monthly Averages:
Assume the data starts on January 1st. Compute the average monthly rainfall using fancy indexing."""

#doesnt allow uneven
#rainByMonth = rainfall.reshape(rainfall, 12)

rainByMonth = np.array_split(rainfall, 12)

for month in rainByMonth:
    print("Avg:", month.mean().round(2))
    print("months vslues :", [int(val) for val in month])
