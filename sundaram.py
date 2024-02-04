import time

def sieve_of_sundaram(max_number = 10):
    # starttime of the script
    starttime = time.time()
    checks_performed = 0
    
    # list of odd numbers < max_number
    nNew = int((max_number - 1) / 2)
    num = [[2*i+1, True, 0] for i in range(nNew + 1)]

    # sieve of sundaram
    for i in range(1, nNew + 1):
        j = i
        while((i + j + 2 * i * j) <= nNew):
            num[i + j + 2 * i * j][1] = False
            num[i + j + 2 * i * j][2] = time.time()-starttime
            j += 1
            checks_performed += 1
        num[i][2] = time.time()-starttime
    
    # output array in standard format
    out = [[i+1, False, 0] for i in range(max_number)]
    for i in range(len(num)):
        out[num[i][0]-1][2] = num[i][2]
        if (num[i][1] == True):
            out[num[i][0]-1][1] = True
    
    # special cases 1 & 2
    out[0][1] = False
    if len(num)>1:
        out[1][1] = True

    # returning list in standard format, runtime and amount of checks
    return out, (time.time()-starttime), checks_performed