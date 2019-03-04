import matplotlib.pyplot as plt
import math
import random


def nextTime(mean):
    return -mean * math.log(1 - random.random())



def singleQueue(alpha, beta, time=480):
    tarrival = 0
    tserve = 0
    currentT = 0
    maxQ = 0
    Q = 1  # initilize the given variables
    while currentT < time:
        if tarrival < tserve:
            tserve = tserve - tarrival
            currentT = currentT + tarrival
            Q = Q + 1
            maxQ = max(maxQ, Q)
            tarrival = nextTime(alpha)  # simulate customer arrival and next arrival
        else:
            tarrival = tarrival - tserve
            currentT = currentT + tserve
            Q = Q - 1
            tserve = nextTime(beta)  # simulate service of a customer and next to be served
        while True:
            if Q != 0:
                break
            else:
                currentT = currentT + tarrival
                Q = Q + 1
                maxQ = max(maxQ, Q)
                tarrival = nextTime(alpha)
    return maxQ


def doubleQueue(alpha, beta, time=480):
    tarrival = 0
    tserve = 0
    tserveS = 0 # time served for the second queue
    currentT = 0
    maxQ = 0
    Q = 1
    Qs = 1 #this is the second queue
    while currentT < time:
        if tarrival < tserve and tarrival < tserveS:
            if Q <= Qs:    #the customers arriving join the shortest queue
                currentT = currentT + tarrival
                tserve = tserve - tarrival
                Q = Q + 1 #add the customer to the queue
                maxQ = max(maxQ, Q) #update maxQ
            else:
                currentT = currentT + tarrival
                tserveS = tserveS - tarrival
                Qs = Qs + 1
                maxQ = max(maxQ, Qs)
            tarrival = nextTime(alpha)   #time of next arrival is scheduled
        else:
            if tserve < tserveS:
                tarrival = tarrival - tserve
                currentT = currentT + tserve
                Q = Q - 1   #customet leaves queue 1
                tserve = nextTime(beta) # generate the next service
            else:
                tarrival = tarrival - tserveS
                currentT = currentT + tserveS
                Qs = Qs - 1  #customer leaves second queue
                tserveS = nextTime(beta) #generate the next service in second teller
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
                tarrival = nextTime(alpha) #add customers on the queues while others are being served
    return maxQ


xSingle = []
ySingle = []
for i in range(10,110):
    xSingle.append(i/10)
    random.seed(101)
    ySingle.append(singleQueue(i/10,4,480)) #plot the results for single queue


xDouble = []
yDouble = []
for i in range(10,110):
    xDouble.append(i/10)
    random.seed(101)
    yDouble.append(doubleQueue(i/10,4,480)) #plot the results for double queue

fig = plt.figure("Improvement on queue")
ax = fig.add_subplot(1,1,1)

plt.plot(xSingle,ySingle,"b-", label="One teller")
plt.plot(xDouble,yDouble,"r-", label="Second teller")
plt.title("Max Queue Length Change With Second Teller")
plt.xlabel("Mean gap customers arriving")
plt.ylabel("Max queue length")
ax.legend()
plt.show()