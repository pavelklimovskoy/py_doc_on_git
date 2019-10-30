num=[2,3,5]

n=6
lim=int(input("your number of prime numbers is "))
k=True

while True:
    for i in num:
        if n%i == 0:
            k=False
            break
    if (k==True):
         num.append(n)
    n+=1
    k=True
    if len(num)>=lim:
        break
            
        
print(num)
print(len(num))
