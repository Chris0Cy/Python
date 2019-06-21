import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections 

dataSet = pd.read_excel('Sales.xlsx', index_col=0)

myNpArray = np.array(dataSet)


col_data = myNpArray[:, 8]

c = collections.Counter(col_data)

fig = plt.figure(1, figsize= (9,2))
ax = fig.add_subplot(132)
ax.set_title("Amount Sold")
plt.bar(list(c.keys())[0],list(c.values())[0])
plt.bar(list(c.keys())[1],list(c.values())[1])
plt.show()

