file_in = open('square.in','r')
file_out = open('square.out','r')



table = []





for i in range(n):
    table.append([])
    for j in range(n):
        table[i].append(0)
        
print(table)


file_in.close()
file_out.close()
