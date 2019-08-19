#cout zero in number
from my_bin_lib import my_bin

n = my_bin(int(input("enter your num: ")),2)
a, b = 0, 0

for i in n:
    if i == '1':
        a += 1
    if i == '0':
        b += 1
         
print("bin_num:"+str(n))
print("number of units:"+str(a))
print("number of zeros:"+str(b))


