#cout zero in number

n = bin(int(input("enter your num: ")))
a, b = 0, 0

for i in n[2:]:
    if i == '1':
        a += 1
    if i == '0':
        b += 1
         
print("bin_num:"+str(n))
print("number of units:"+str(a))
print("number of zeros:"+str(b))


