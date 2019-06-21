import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

inFile = pd.read_csv('Disputed_Essay_data.csv')

dataSetPandaFrame = pd.DataFrame(inFile)

dataSetPandaFrame = dataSetPandaFrame.drop(dataSetPandaFrame.index[62:72])

dataSetPandaFrame = dataSetPandaFrame.drop('filename', axis= 1)

print("the data for dataSetPandaFrame is:")
print(dataSetPandaFrame)


disputeVariableDataSet = dataSetPandaFrame[:11]

disputeVariableDataSet = disputeVariableDataSet.drop('author', axis=1)

print("the data for disputeVariableDataSet is:")
print(disputeVariableDataSet)


dataSet = dataSetPandaFrame[11:]

print("the data for dataSet is:")
print(dataSet)


targetVariable = dataSet.author

print("the data for targetvariable is:")
print(targetVariable)

dataSet = dataSet.drop('author',axis = 1)

print("the data for dataSet after author dropped")
print(dataSet)

x_train, x_test, y_train, y_test = train_test_split(dataSet,targetVariable,test_size=0.5,random_state=1)

treeModel = tree.DecisionTreeClassifier()

treeModel = treeModel.fit(x_test,y_train)

x_prediction = treeModel.predict(x_test)

print("the data for x_prediction is:")
print (x_prediction)

print ("the confusing matrix for this algorithm ")
print (
pd.DataFrame(
    confusion_matrix(y_test,x_prediction),
    columns=['Hamilton','Madison'],
    index=['Hamilton','Madison']
)
)
print ("the accuaracy of this algorithm is:")
print (accuracy_score(y_test,x_prediction))

