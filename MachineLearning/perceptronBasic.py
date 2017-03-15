import numpy as np

#creates constant for data size
columns = 100
rolls = 2

# creates random value table
X = np.random.randn(columns,rolls)
print "this is value of X variable"
print X

#creates a vector(columns) of ones
ones = np.ones((columns, 1))
print "this is the value of ones"
print ones

#create a new data set by adding one to the old data set which is X
XwithOnes = np.concatenate((ones, X), axis=1)
print "This is the value of XwithOnes"
print XwithOnes

#random initialize a weight(roll) vector
weight = np.random.rand(rolls + 1)
print "This is the value of weight"
print weight

#matrix multication using numpy dot function
results = XwithOnes.dot(weight)
print "this is the value of results"
print results

#sigmoid function
def sigmoid(results):
    return 1/(1 + np.exp(-results))

print sigmoid(results)
