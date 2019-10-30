sign = 1
res = 0

for i in range(0, 1000):
    res = res + sign/(2*i + 1)
    sign = -sign

print("PI=" + str(res*4))
