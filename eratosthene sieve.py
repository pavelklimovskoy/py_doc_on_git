num = [i for i in range(2,100)]

for i in num:
    for j in num:
        if j==i:
            continue
        if j%i == 0:
            num.remove(j)
            
print(num)
