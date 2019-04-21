##this is a line chart including the performance by month 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 
 
data = np.genfromtxt("Sales.csv", delimiter=',', skip_header=1, dtype="str")
##11 = units sold
newarr = data[:,[1,3,9,11]]
 
Funiture_sales_13 = {"Jan-2013": 0,
                "Feb-2013": 0,
                "Mar-2013": 0,
                "Apr-2013": 0,
                "May-2013": 0,
                "Jun-2013": 0,
                "Jul-2013": 0,
                "Aug-2013": 0,
                "Sep-2013": 0,
                "Oct-2013": 0,
                "Nov-2013": 0,
                "Dec-2013": 0,
}
Electronics_sales_13 = {"Jan-2013": 0,
                "Feb-2013": 0,
                "Mar-2013": 0,
                "Apr-2013": 0,
                "May-2013": 0,
                "Jun-2013": 0,
                "Jul-2013": 0,
                "Aug-2013": 0,
                "Sep-2013": 0,
                "Oct-2013": 0,
                "Nov-2013": 0,
                "Dec-2013": 0,
}
Funiture_sales_14 = {"Jan-2014": 0,
                "Feb-2014": 0,
                "Mar-2014": 0,
                "Apr-2014": 0,
                "May-2014": 0,
                "Jun-2014": 0,
                "Jul-2014": 0,
                "Aug-2014": 0,
                "Sep-2014": 0,
                "Oct-2014": 0,
                "Nov-2014": 0,
                "Dec-2014": 0,
}
Electronics_sales_14 = {"Jan-2014": 0,
                "Feb-2014": 0,
                "Mar-2014": 0,
                "Apr-2014": 0,
                "May-2014": 0,
                "Jun-2014": 0,
                "Jul-2014": 0,
                "Aug-2014": 0,
                "Sep-2014": 0,
                "Oct-2014": 0,
                "Nov-2014": 0,
                "Dec-2014": 0,
}
 
for row in newarr:
    for col in row:
        if (row[0] == "2013") and (row[2] == "Furniture"):
            month = row[1] + "-" + row[0]
            Funiture_sales_13[month] += int(row[3])
        elif (row[0] == "2013") and (row[2] == "Electronic"):
            month = row[1] + "-" + row[0]
            Electronics_sales_13[month] += int(row[3])
        elif (row[0] == "2014") and (row[2] == "Furniture"):
            month = row[1] + "-" + row[0]
            Funiture_sales_14[month] += int(row[3])
        elif (row[0] == "2014") and (row[2] == "Electronic"):
            month = row[1] + "-" + row[0]
            Electronics_sales_14[month] += int(row[3])
 
 
## get the months
m = [x[:3] for x in list(Funiture_sales_13.keys())]
 
 
fig, ax = plt.subplots()
plt.plot([x for x in list(Funiture_sales_13.values())], label="Furniture 2013")
plt.plot([x for x in list(Funiture_sales_14.values())], label="Furniture 2014")
plt.plot([x for x in list(Electronics_sales_13.values())], label="Electronics 2013")
plt.plot([x for x in list(Electronics_sales_14.values())], label="Electronics 2014")
plt.xticks(np.arange(0, len(m)+1), m)  ## label x axis with months
 
## annotate each line
for x, y in enumerate(list(Funiture_sales_13.values())):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,2), ha='left', fontsize=7)
for x, y in enumerate(list(Funiture_sales_14.values())):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,2), ha='right', fontsize=7)
for x, y in enumerate(list(Electronics_sales_13.values())):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,2), ha='center', fontsize=7)
for x, y in enumerate(list(Electronics_sales_14.values())):
    label = y
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,2), ha='right', fontsize=7)
 
 
ax.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
 
