# I'm going to try working with Boston Housing data
import pandas as pd

# 1st step is to convert the txt file into a csv
read_file = pd.read_csv (r'./boston_housing.txt')
read_file.to_csv (r'./boston_housing.csv', index=None)

print("done")


# 2nd step is to take a look at the data

# 3rd step is to try to apply a regression model
# using sk kit and ML studd