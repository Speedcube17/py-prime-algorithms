import time

def sieve_of_erastosthenes(max_number = 10): 
    starttime = time.time()
    num = [[i+1, True, 0] for i in range(max_number)]
    
    # special case 1
    num[0][1]=False
    
    # sieve of erastosthenes
    for i in range(1, round((max_number**(1/2))+0.5)): #square root of max_num+0.5 to round up to nearest int
        if num[i][1]==True: #if i is saved as prime
            num[i][2] = time.time()-starttime
            #print("Crossed out multiples of "+str((i+1))+" in "+str(time.time()))
            
            j=2 #multiplication factor
            while ((i+1)*j)<=max_number: #while the prime i+1 multiplied with j is smaller than max
                num[(i+1)*j-1][1]=False #set multiples of i to composite number
                j+=1 #increment j
    
    return num, (time.time()-starttime)