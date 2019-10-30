from pylab import *

x=[]
y=[]
n=1
sm=""
num=[]

file = open('list.txt')
line=file.readline()

while line:
    for char in line:
        if char != "	" and char !="\n":
            num.append(char)
        else:
            for i in num:
                sm=sm+i
                
            if n %2 != 0:
                x.append(float(sm))
                n+=1
                num=[]
                sm=""
            else:
                y.append(float(sm))
                n+=1
                num=[]
                sm=""

    line=file.readline()

file.close

grid()
plot(x,y,'b',linewidth=1)
show()
