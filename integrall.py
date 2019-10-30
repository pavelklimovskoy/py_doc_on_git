
string=input("enter func like:x^p+q:")
b=int(input("enter low limit:"))
a=int(input("enter high limit:"))

for i in range(len(string)):
    if (string[i] == "x" and string[i+1] =="^"):
        p=int(string[i+2])
    if string[i]=="+":
       q=int(string[i+1])

def in_funct(x):
    global p, q
    return x**p+q

def integrall_by_func(x,y):
    d=0.0001
    res=0
    while x<y:
        x=x+d
        res=res+in_funct(x)
    return round(res*d,2)
        
print(integrall_by_func(b,a))



