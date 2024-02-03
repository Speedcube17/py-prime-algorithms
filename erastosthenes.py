import time

def sieve_of_erastosthenes(max_number = 10): 
    # num[0]=1; num[1]=2; ...
    num = [None] * (max_number)
    for a in range(max_number): 
        num[a] = True
    
    # special case 1
    num[0]=False
    
    # sieve of erastosthenes
    for i in range(1, round((max_number**(1/2))+0.5)): #square root of max_num+0.5 to round up to nearest int
        if num[i]==True: #if i is saved as prime
            j=2 #multiplication factor
            while ((i+1)*j)<=max_number: #while the prime i+1 multiplied with j is smaller than max
                num[(i+1)*j-1]=False #set multiples of i to composite number
                j+=1 #increment j
    
    return num

print(sieve_of_erastosthenes(121))