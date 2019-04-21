#bar chart which shows the compare eletronics vs furniture 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections 

dataSet = pd.read_excel('Sales.xlsx', index_col=0)

myNpArray = np.array(dataSet)

lineGraphData = myNpArray[:,[8,11]]

## print(lineGraphData)

totalSumOfProducts = {"Electronic" : 0, "Furniture": 0}
print(lineGraphData[0][1])

for row in lineGraphData:
    for col in row:
        if(row[0] == "Electronic"):
            totalSumOfProducts["Electronic"] += row[1]
        else:
            totalSumOfProducts["Furniture"] += row[1]

labels = list(totalSumOfProducts.keys())[0], list(totalSumOfProducts.keys())[1]
size = [list(totalSumOfProducts.values())[0], list(totalSumOfProducts.values())[1]]
fig1, ax1 = plt.subplots()
ax1.pie(size, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  

plt.show()
