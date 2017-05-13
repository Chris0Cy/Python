import numpy as np
import pandas as pd

#getting data form file
def getData():

    #storing data in a variable
    dataFile = pd.read_csv('ecommerce_data.csv')
    
    #processing data into numpy matrix
    data = dataFile.as_matrix()

    #extracting information form data
    #store n to n-1 data in X
    X = data[:,:-1]

    #score last line in Y
    Y = data[:,-1]

    #normalized
    #X1 = x1 - x1(mean) / X1 standard deviation
    X[:,1] = (X[:,1]-X[:,1].mean() / X[:,1].std())
    
    #same for X2
    X[:,2] = (X[:,2]-X[:,2].mean() / X[:,2].std())

    #working on the time of the day column
    #getting shape of orginal X
    N, D = X.shape
    X2 = np.zeros((N,D+3)) #four different catagory value

    X2[:,0:(D-1)] = X[:,0:(D-1)] # ask professor

    for n in xrange(N): # ask professor 
        t = int(X[n,D-1])
        X2[n,t+D-1] = 1

    return X2, Y

def get_binary_data():
    X, Y = getData()
    X2 = X[Y <= 1]
    Y2 = Y[Y <= 1]
    return X2, Y2