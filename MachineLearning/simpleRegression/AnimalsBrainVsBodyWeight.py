#imports all the dependency

#for data processing
import pandas as pd

#training or modeling library
from sklearn import linear_model

#for plotting 
import matplotlib.pyplot as plt

#reading data from file using pandas
dataFromFile = pd.read_fwf('brain_body.txt')
x_values = dataFromFile[['Brain']]
y_values = dataFromFile[['Body']]

#train model on data
x_value_regression = linear_model.LinearRegression()
x_value_regression.fit(x_values,y_values)

#plotting the graph
plt.scatter(x_values, y_values)
plt.plot(x_values,x_value_regression.predict(x_values))
plt.show()
