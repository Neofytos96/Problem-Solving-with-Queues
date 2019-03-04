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

xaxis = []
yaxis = []
for i in range (11,110):
    xaxis.append(i/10)
    random.seed(101)
    yaxis.append(singleQueue(i/10,4,480))

xaxis625 = []
yaxis625 = []
for i in range (11,110):
    xaxis625.append(i/10)
    random.seed(101)
    yaxis625.append(singleQueue(i/10,1.5,480))


xaxis25 = []
yaxis25 = []
for i in range (11,110):
    xaxis25.append(i/10)
    random.seed(101)
    yaxis25.append(singleQueue(i/10,3,480))

xaxis50 = []
yaxis50 = []
for i in range (11,110):
    xaxis50.append(i/10)
    random.seed(101)
    yaxis50.append(singleQueue(i/10,2,480))


fig = plt.figure("Improvenet on queue")
ax = fig.add_subplot(1,1,1)

plt.plot(xaxis, yaxis, "b-", label="Normal Queue")
plt.plot(xaxis625, yaxis625, "g-", label="Reduce service time by 62.5%")
plt.plot(xaxis50, yaxis50, "y-", label="Reduce service time by 50%")
plt.plot(xaxis25, yaxis25, "r-", label="Reduce service time by 25%")
plt.title("Max queue length change from new equipment purchase ")
plt.xlabel("Mean Gap Customers Arriving")
plt.ylabel("Max Queue Length")
ax.legend()
plt.show()




