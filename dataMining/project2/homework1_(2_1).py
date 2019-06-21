import numpy as np 
import pandas as pd 

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score


#read from data
data = pd.read_csv("Students Academic Performance.csv")

#deleting the "Class" column from table
Features = data.drop('Class',axis=1)

#selecting predict variable
Target = data['Class']

#creates a label using sklearn LabelEnconder
label = LabelEncoder()
Cat_Colums = Features.dtypes.pipe(lambda Features: Features[Features=='object']).index
for col in Cat_Colums:
    Features[col] = label.fit_transform(Features[col])


#splitting data to 0.2 for testing and 0.8 for training
X_train, X_test, y_train, y_test = train_test_split(Features, Target, test_size=0.2, random_state=52)

#creates the logistics regressions
logisticsRegressionModel = LogisticRegression()

#run logistic regression between x and y value.
logisticsRegressionModel.fit(X_train,y_train)

# use logistics regression model and run the prediction on x_test variable
Prediction = logisticsRegressionModel.predict(X_test)
Score = accuracy_score(y_test,Prediction)
Report = classification_report(y_test,Prediction)

#output to screen
print(Prediction)

print("Score of the model is: ")
print(Score)
print(Report)
