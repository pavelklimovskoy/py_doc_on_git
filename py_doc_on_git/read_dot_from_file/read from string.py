string="4.950337E-5"
num=[]
n=0
sm=""


for char in string:
    if char != "E":
        num.append(char)
        n+=1
    else:
        for i in num:
            sm=sm+i
        n+=1

    if (n==len(string)-2):

        k=string[n]
    elif (n==len(string)-1):
        k=k+string[n]
        
print(float(sm)*(10**(int(k)) ))


