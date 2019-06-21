import pandas as pd 
import numpy as np
from math import log


def readingInDataUsingPandas(filePath):
    return pd.read_csv(filePath).as_matrix()


def getLabelAndDataFromFile(pandasMatrix):
    
    label_train = pandasMatrix[0:,0]
    data_train = pandasMatrix[0:,1:]
    
    return label_train, data_train

def  extract_terms (dataSet):

    results = [[0]*2 for i in range(len(dataSet))]
    score = [0]*10
    return results, score


def convert_to_binary( trainingData ):
    return (trainingData >= 128 ).astype( int )

def training_nb( label_train, data_train_bi ):

    train, priors = extract( label_train, data_train_bi )

    for i in range( 10 ):
        for j in range ( 784 ):
            train[i][j] = ( train[i][j] + 0.01 ) / ( priors[i] + 0.02 )
        priors[i] = priors[i] / len( label_train )

    return train, priors


def extract( labelTraining, testTraining ):

    train = [[0]*785 for _ in range(10)]
    priors = [0]*10
    for i in range( len( labelTraining ) ):
        priors[labelTraining[i]] = priors[labelTraining[i]] + 1
        for j in range ( 784 ):
            train[labelTraining[i]][j] = train[labelTraining[i]][j] + testTraining[i][j]

    return train, priors

def apply_nb( train, priors, dataTrainingB ):

    results, score = extract_terms ( dataTrainingB )
    for i in range( len( dataTrainingB ) ):
            for j in range( len( priors ) ):
                score[j] = log( priors[j] )
                for k in range( 784 ):
                    if dataTrainingB[i][k] == 1:
                        score[j] += log( train[j][k] )
                    else:
                        score[j] += log ( 1. - train[j][k] )
            results[i] = [i+1, np.argmax( score )]

    return results


def runModel():

    train_dataset = readingInDataUsingPandas( 'train.csv' )
    test_dataset = readingInDataUsingPandas( 'test.csv' )

    trainingLabel, trainingData = getLabelAndDataFromFile( train_dataset )


    trainingDataB = convert_to_binary( trainingData )
    train, priors = training_nb( trainingLabel, trainingDataB )

    test_dataset_bi = convert_to_binary( test_dataset )
    results = apply_nb( train, priors, test_dataset_bi )
    
    print (results)

    
if __name__ == '__main__':   
    runModel()
    print("finished")

