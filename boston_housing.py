# I'm going to try working with Boston Housing data

import pandas as pd

# 1st step is to convert the txt file into a csv
with open('./boston_housing2.txt') as f:
    # Read space-delimited file and replace all empty spaces by commas
    data = f.read().replace('\n  ', ',')
    # Write the CSV data in the output file
    print(data, file=open('data1.txt', 'w'))

with open('./data1.txt') as f:
    # Read space-delimited file and replace all empty spaces by commas
    # data = f.read().replace(' ', ',')
    # Write the CSV data in the output file
    line_lst = []
    for line in f.readlines():
        # strips leading white spaces
        strip_white_spaces = line.lstrip()
        # replaces longer spaces with a single space
        strip_white_spaces = strip_white_spaces.replace("   ", " ")
        strip_white_spaces = strip_white_spaces.replace("  ", " ")
        # replace single white spaces with a comma
        strip_white_spaces = strip_white_spaces.replace(" ", ",")
        # fix instances of double comma
        strip_white_spaces = strip_white_spaces.replace(",,", ",")

        line_lst.append(strip_white_spaces)

    lines = ''.join(line_lst)
    print(lines, file=open('data2.csv', 'w'))


data_frame = pd.read_csv("data2.csv", sep=',',
                         names=['Crime', 'Zone', 'Indus', 'Chas', 'NOX', 'RM',
                                'age','dis', 'rad', 'tax', 'ptratio', 'b',
                                'ltstat', 'medv' ])

data_frame.to_csv('final_data.csv', index=None)



print("done")


# 2nd step is to take a look at the data


# 3rd step is to try to apply a regression model
# using sk kit and ML studd