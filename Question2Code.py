import matplotlib.pyplot as plt

def theoreticalMeanQueueLength(alpha, beta):
    if alpha == beta or alpha == 0:
        return (-1)
    else:
        return (beta/alpha)/(1-(beta/alpha))




xaxis = []
yaxis = []
for i in range(11, 101):
    xaxis.append(i/10) # put on the xaxis the mean gap customer arrival
    yaxis.append(theoreticalMeanQueueLength(i/10, 1)) #put the mean queue length on y axis

fig = plt.figure("Queue Improvement")
plt.plot(xaxis,yaxis, "b-")
plt.title("Mean queue change with customer arrival")
plt.xlabel("Mean Gap Customers Arriving")
plt.ylabel("Mean Queue Length")
plt.show()
