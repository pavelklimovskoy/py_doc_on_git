num_1=[2,5,11,4,1,3,10,7,6,13,0,12,9,8]
num_2=num_1[:]
num_fin=[]
while (len(num_fin)!=len(num_1)):
    num_fin.append(min(num_2))
    num_2.remove(min(num_2))
print(num_fin)

