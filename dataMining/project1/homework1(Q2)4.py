import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 
data = np.genfromtxt("Sales.csv", delimiter=',', skip_header=1, dtype="str")

## start here for bar graph
piecesOfFurniture, count = np.unique(data[:,[8]], return_counts=True)
itemssold = dict(zip(piecesOfFurniture, count))

labels = list(itemssold.keys())[0], list(itemssold.keys())[1], list(itemssold.values())[2] ,list(itemssold.values())[3] ,list(itemssold.values())[4]
size = [list(itemssold.values())[0], list(itemssold.values())[1],list(itemssold.values())[2],list(itemssold.values())[3],list(itemssold.values())[4]]
fig1, ax1 = plt.subplots()
ax1.pie(size, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  

plt.show()
