import numpy as np
from dataProcessingFromFile import get_binary_data

X, Y = get_binary_data()

#initialization of shape
D = X.shape[1]

#initialization of weight 
W = np.random.randn(D)

#initalization of Bias
b = 0

#defining sigmoid function
def sigmoid(a):
    return 1 / (1 + np.exp(-a))

#defining forward function
def forward(X,W,b):
    return sigmoid(X.dot(W)+b)

#storing value after processed using sigmoid
P_Y_given_X = forward(X,W,b)

#makeing prediction function
predictions = np.round(P_Y_given_X)

#defining classication_rate
#return 1 or 0 , note not boolean
def classication_rate(Y,P):
    return np.mean(Y == P)

print "Score", classication_rate(Y, predictions)