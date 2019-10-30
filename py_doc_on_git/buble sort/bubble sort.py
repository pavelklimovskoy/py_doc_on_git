num=[49,40,28,26,20,48,10,31,0,47,33,7,46,8,45.5,30,39,42,6,43,9,32,5,44,2,45,4,27,3,38,1,41,19,11,18,12,34,29,16,13,35,15,14,17,21,37,22,24,23,25,36]
n,k=0,0
print("start"+str(num))
while True:
    if (num[(n)]>num[n+1]):       
        x=num[n]
        y=num[n+1]
        num[n+1]=x
        num[n]=y
        if (n<(len(num)-2)):
            n=n+1
        else:
            n=0
        #print(num)
    else:
        if (n<(len(num)-2) ):
            n=n+1
        else:
            n=0
            k=k+1
            if (k>=(len(num))-1):
                break
            #print(n)
        #print(num)

#print(k)
#print(n)
print("end"+str(num))

    





