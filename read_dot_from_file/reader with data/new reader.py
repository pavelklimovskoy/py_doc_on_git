from pylab import *

x, y = [], []

file = open('list.txt')
line = file.readline().split('\t')
while line != ['']:
    x.append(float(line[0]))
    y.append(float(line[1]))
    line = file.readline().split('\t')

file.close()

grid()
plot(x,y,'b',linewidth=0.5)
show()

