n=abs(int(input('your_num_=')))
def sq_rt(x):
    n=0
    sq_list=[i**2 for i in range(n+1)]
    while True:
        if x>sq_list[n]:
            n=n+1
            sq_list=[i**2 for i in range(n+2)]
        elif x==sq_list[n]:
            return(int(n))
            break
        elif x<sq_list[n+1]:
            b=abs(x-sq_list[n-1])
            r=(n-1)+(b/(2*(n-1)))
            return(float(r))
            break

            

print('sq_rt('+str(n)+')='+str(sq_rt(n)))
