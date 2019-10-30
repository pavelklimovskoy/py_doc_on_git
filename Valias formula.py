res = 1

for n in range(1, 10000):
    
    res = res * ((2*n)**2)/((2*n - 1)*(2*n + 1))
    
print("PI="+str(2*res))
