line="1,3,2,4,3,7,4,9,5,0,6,8"
x=[]
y=[]
n=1

for i in line:
    if i != ",":
        num=i

    else:
        if n %2 != 0:
            x.append(int(num))
            n+=1
        else:
            y.append(int(num))
            n+=1
        
print("string="+line)
print("sorted x from string="+str(x))
print("sorted y from string="+str(y))
