import time

def sieve_of_atkin(max_number):
    # starttime of the script
    starttime = time.time()
    checks_performed = 0
    
    # create list of all numbers < max_number
    num = [[i+1, False, 0] for i in range(max_number)]
    for i in range(0, max_number):
        num[i][1] = False
    
    # sieve of atkin
    i = 1
    while i**2 <= max_number:
        j = 1
        while j**2 <= max_number:
            n = (4*i**2) + (j**2)
            if (n <= max_number and (n % 12 == 1 or n % 12 == 5)):
                num[n-1][1] ^= True
                num[n-1][2] = time.time()-starttime
                checks_performed += 1

            n = (3*i**2) + (j**2)
            if n <= max_number and n % 12 == 7:
                num[n-1][1] ^= True
                num[n-1][2] = time.time()-starttime
                checks_performed += 1

            n = (3*i**2) - (j**2)
            if (i > j and n <= max_number and n % 12 == 11):
                num[n-1][1] ^= True
                num[n-1][2] = time.time()-starttime
                checks_performed += 1
            
            j += 1
        i += 1

    # crossing out square numbers
    i = 5
    while i * i <= max_number:
        if num[i-1][1]:
            for j in range(i * i, max_number+1, i * i):
                num[j-1][1] = False

        i += 1
        
    # special cases 2 & 3
    if len(num) > 1: 
        num[1][1] = True
        if len(num) > 2: 
            num[2][1] = True

    # return list, runtime and amount of checks
    return num, (time.time() - starttime), checks_performed