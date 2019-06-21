import numpy as np
import csv
from sklearn.neighbors import KNeighborsClassifier


def read_data(f, header=True, test=False):
    data = []
    labels = []

    csv_reader = csv.reader(open(f, "r"), delimiter=",")
    index = 0
    for row in csv_reader:
        index = index + 1
        if header and index == 1:
            continue

        if not test:
            labels.append(int(row[0]))
            row = row[1:]

        data.append(np.array(np.int64(row)))

    return (data, labels)


def runModel(train, test, labels):

    train_mat = np.mat(train)

    knn = KNeighborsClassifier(n_neighbors=10, algorithm="kd_tree")
    print (knn.fit(train_mat, labels))

    results = knn.predict(test)

    return results



if __name__ == '__main__':
    train, labels = read_data("train.csv")
    test, tmpl = read_data("test.csv", test=True)
    predictions = runModel(train, test, labels)
    print (predictions)
