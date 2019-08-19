def my_bin(num,base):
    bin_num = ''
    while num % base < base and num != 0 :
        bin_num = bin_num + str(int(num % base))
        num = (num - (num % base)) / base
    return bin_num[::-1]
    
