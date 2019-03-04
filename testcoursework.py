import csv
import math
import random


def nextTime(mean):
    return -mean * math.log(1 - random.random())
import re
import string
def readExperimentParameters(filename):
     reader = csv.reader(open(filename))
     next(reader)
     rowlist = []
     new_list = []
     finallist = []
     for row in reader:
         rowlist.append(row)
     new_list = [list(filter(None, lst)) for lst in rowlist]
    # print(new_list)
     for i in new_list:
          #print(i)
          if i[3] != " h":
              i.remove(i[3])
          else:
             i[2] = int(i[2]) *60
             i.remove(i[3])
     for values in new_list:
         values = list(map(int, values))
         finallist.append(tuple(values))


     return finallist




#print(readExperimentParameters("experiments.csv")[0])


def doubleQueue(alpha, beta, time=480):
    tarrival = 0
    tserve = 0
    tserveS = 0
    currentT = 0
    maxQ = 0
    Q = 1
    Qs = 1
    while currentT < time:
        if tarrival < tserve and tarrival < tserveS:
            if Q <= Qs:
                currentT = currentT + tarrival
                tserve = tserve - tarrival
                Q = Q + 1
                maxQ = max(maxQ, Q)
            else:
                currentT = currentT + tarrival
                tserveS = tserveS - tarrival
                Qs = Qs + 1
                maxQ = max(maxQ, Qs)
            tarrival = nextTime(alpha)
        else:
            if tserve < tserveS:
                tarrival = tarrival - tserve
                currentT = currentT + tserve
                Q = Q - 1
                tserve = nextTime(beta)
            else:
                tarrival = tarrival - tserveS
                currentT = currentT + tserveS
                Qs = Qs - 1
                tserveS = nextTime(beta)
        while True:
            if Q != 0 and Qs != 0:
                break
            else:
                currentT = currentT + tarrival
                if Q <= Qs:
                    Q = Q + 1
                    maxQ = max(maxQ, Q)
                else:
                    Qs = Qs + 1
                    maxQ = max(maxQ, Qs)
                tarrival = nextTime(alpha)
    return maxQ


random.seed(57)
print("single is 3. Double is: ",doubleQueue(10, 3, 480))
random.seed(101)
print("single is 6. Double is: ",doubleQueue(5, 3, 480))
random.seed(101)
print("single is 6. Double is:",doubleQueue(5, 3))
random.seed(935)
print("single is 10. Double is:",doubleQueue(10, 9, 280))
#assumptio is that both tellers work at the same rate




def singleQueue(alpha, beta, time=480):
    tarrival = 0
    tserve = 0
    currentT = 0
    maxQ = 0
    Q = 1
    while currentT < time:
        if tarrival < tserve:
            tserve = tserve - tarrival
            currentT = currentT + tarrival
            Q = Q + 1
            maxQ = max(maxQ, Q)
            tarrival = nextTime(alpha)
        else:
            tarrival = tarrival - tserve
            currentT = currentT + tserve
            Q = Q - 1
            tserve = nextTime(beta)
        while True:
            if Q != 0:
                break
            else:
                currentT = currentT + tarrival
                Q = Q + 1
                maxQ = max(maxQ, Q)
                tarrival = nextTime(alpha)
    return maxQ

#random.seed(101)
#print("single max", singleQueue(5,3,480))

