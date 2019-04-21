# extract information from data using different datas contain within the spreadsheet

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections 

dataSet = pd.read_excel('Sales.xlsx', index_col=0)

dataSetPanda = pd.DataFrame(dataSet)
dataSetNp = np.array(dataSet)

cubeData = dataSetNp[:,[8,0,2,4]]


"""
Slice operation: compute the revenue for Laptop during January of 2013 in each state.
"""
#part 1 create a 2D of invidual states


stateCol = np.unique(dataSetNp[:,[4]])
stateCol = np.reshape(stateCol,(5,1))
temp = np.zeros(5)
temp = np.reshape(temp, (5,1))
stateCol = np.hstack((stateCol,temp))
stateColQuestionTwo = stateCol
productCol = np.unique(dataSetNp[:,[7]])
productCol = np.reshape(productCol, (5,1))
productCol = np.hstack((productCol,temp,temp))
MonthlyAndProduct = np.hstack((productCol,temp,temp,temp,temp,temp,temp,temp,temp,temp,temp))


for row in dataSetNp:
    for col in row:
        if(((row[0] == 2013) and (row[2] == "Jan")) and (row[7] == "Laptop" )):
            for r in stateCol:
                if (row[4] == r[0]):
                    r[1] += row[11]

print("question 3 part 1")
print ("revenue for laptop during jan 2013")
print (stateCol)
print()

"""
Dice operation: compute the revenue for the furniture products (Mattress
and Chair) during the second quarter (April, May and June) of 2014 in each
state
"""

# part 2
for row in dataSetNp:
    for col in row:
        if(((row[0] == 2014) and ((row[2] == "Apr") or (row[2] == "May") or (row[2] == "Jun") )and ((row[7] == "Chair" ) or (row[7] == "Mattress" )))):
            for r in stateColQuestionTwo:
                if (row[4] == r[0]):
                    r[1] += row[11]


print("question 3 part 2")
print("product, sales")
print (stateColQuestionTwo)
print()

"""
Rollup operation: compute the annual revenue for each product and
collapse the state and month dimensions
"""


# part 3

for row in dataSetNp:
    for col in row:
        for r in productCol:
            if (row[7] == r[0]) and (row[0] == 2013):
                r[1] += row[11]
            elif (row[7] == r[0]) and (row[0] == 2014):
                r[2] += row[11]



print ("question 3 part 3")
print ("product , year 2013, 2014")
print (productCol)
print()

"""
Drilldown operation: compute the annual and monthly revenue for each
product and collapse the state dimension.
"""

# part 4

for row in dataSetNp:
    for col in row:
        for r in MonthlyAndProduct:
            if (row[7] == r[0]):
                r[row[1]] += row[11]

MonthlyAndProduct = np.hstack((productCol, MonthlyAndProduct[:,1:]))
print("product, 2013,2014, jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec")
print (MonthlyAndProduct)
