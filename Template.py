import random
import math
import csv


def nextTime(mean):
    return -mean * math.log(1 - random.random())


def theoreticalMeanQueueLength(alpha, beta):
    """
    >>> theoreticalMeanQueueLength(10, 2)
    0.25
    >>> theoreticalMeanQueueLength(5, 1)
    0.25
    >>> theoreticalMeanQueueLength(4, 2)
    1.0
    >>> theoreticalMeanQueueLength(5.5, 1.3)
    0.3095238095238095
    >>> theoreticalMeanQueueLength(5.5, 0)
    0.0
    >>> theoreticalMeanQueueLength(1, 1)
    -1
    >>> type(theoreticalMeanQueueLength(10, 2))
    <class 'float'>
    """

    if alpha == beta or alpha == 0:
        return (-1)
    else:
        return (beta/alpha)/(1-(beta/alpha)) #using the given fromula calculates the result


def checkMean(mean, iterations=10000):
    """
    >>> random.seed(57)
    >>> checkMean(5, 10)
    6.309113224728108
    >>> random.seed(57)
    >>> checkMean(5, 1000)
    4.973347344130324
    >>> random.seed(57)
    >>> checkMean(5, 100000)
    4.988076126529703
    >>> random.seed(57)
    >>> checkMean(195, 100000)
    194.53496893466047
    >>> random.seed(57)
    >>> checkMean(195)
    196.71853828860912
    >>> random.seed(57)
    >>> checkMean(31)
    31.273203522804728
    >>> type(checkMean(31, 5))
    <class 'float'>
    """
    # Add code here
    temp = 0
    for i in range(1, iterations+1):
        temp += nextTime(mean)  #iterate through the number of iterations given

    return temp/ iterations



def readExperimentParameters(filename):
    """
    >>> readExperimentParameters('experiments.csv')[0]
    (10, 2, 480)
    >>> len(readExperimentParameters('experiments.csv'))
    5
    >>> readExperimentParameters('experiments.csv')[3]
    (20, 2, 480)
    >>> readExperimentParameters('experiments.csv')[2]
    (20, 15, 240)
    >>> type(readExperimentParameters('experiments.csv')[1])
    <class 'tuple'>
    """
    # Add code here
    reader = csv.reader(open(filename)) #reads the csv file
    next(reader)
    rowlist = []
    finallist = []
    for row in reader:
        rowlist.append(row) #iterate through the rows of the csv file and append the values in rowlist
    new_list = [list(filter(None, lst)) for lst in rowlist] #removes the empty elements from rowlist
    for i in new_list:
        if i[3] != " h":
            i.remove(i[3]) #removes the cells that don't contain the character "h"
        else:
            i[2] = int(i[2]) * 60 #finds the character h and multiplies the cell next to it by 60
            i.remove(i[3])
    for values in new_list:
        values = list(map(int, values)) #converts all the list items to integers
        finallist.append(tuple(values))#append them to the final list as tuples

    return finallist



def singleQueue(alpha, beta, time=480):
    """
    >>> random.seed(57)
    >>> singleQueue(10, 3, 480)
    3
    >>> random.seed(101)
    >>> singleQueue(5, 3, 480)
    6
    >>> random.seed(101)
    >>> singleQueue(5, 3)
    6
    >>> random.seed(935)
    >>> singleQueue(10, 9, 280)
    10
    >>> type(singleQueue(10, 9, 280))
    <class 'int'>
    """
    # Add code here
    tarrival = 0
    tserve = 0
    currentT = 0
    maxQ = 0
    Q = 1   #initilize the given variables
    while currentT < time:
        if tarrival < tserve:
            tserve = tserve - tarrival
            currentT = currentT +tarrival
            Q = Q+1
            maxQ = max(maxQ, Q)
            tarrival = nextTime(alpha)  #simulate customer arrival and next arrival
        else:
            tarrival = tarrival - tserve
            currentT = currentT + tserve
            Q = Q -1
            tserve = nextTime(beta) #simulate service of a customer and next to be served
        while True:
            if Q != 0:
                break
            else:
                currentT = currentT +tarrival
                Q = Q +1
                maxQ = max(maxQ, Q)
                tarrival = nextTime(alpha)
    return maxQ




