import csv
import random
import math
import operator

def loadDataset(filename, split, traningSet = [], testSet = []):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                traningSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

def getNeighbors(traningSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(traningSet)):
        #testinstance
        dist = euclideanDistance(testInstance,traningSet[x],length)
        distances.append((traningSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
        return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return  sortedVotes[0][0]


def getAccuracy(testSet , predictions):
    correct = 0
    for x in range (len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    traningSet = []
    testSet = []
    split = 0.67
    loadDataset(r'irisdata.txt',split,traningSet,testSet)
    print('Train set :' + repr(len(traningSet)))
    print('Test set: ' + repr(len(testSet)))
    print('Test set: ' + repr(testSet))
    predictions = []
    k = 3
    for x in range(len(testSet)):
        # traningsettraningSet[x]
        neighbors = getNeighbors(traningSet,testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)

    print('predictions: ' + repr(predictions))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy:' + repr(accuracy) + '%')

if __name__ == '__main__':
    main()