import time
from check_primes import check_file_primes
from erastosthenes import sieve_of_erastosthenes

primes_smaller_max = int(input("Check primes below n, n="))
if primes_smaller_max > 100000000: 
    print("Error: Control Script maximum reached!")
    quit()

name_of_file = str(time.ctime(time.time())).replace(" ","_").replace(":","-")+".txt"
f = open(name_of_file, "w")    #create new file with starttime (before calculating)

output_of_eras = sieve_of_erastosthenes(primes_smaller_max)    #calculating with sieve of erastosthenes
eras_prime = output_of_eras[0]

# formatting an writing to txt
for i in range(len(eras_prime)):    #for sublists in main list
    line = "Num "+str(eras_prime[i][0])+" is prime: "+str(eras_prime[i][1])
    if type(eras_prime[i][2])!=type(0):                     #if a prime number was found and sieved
        line+=", Operation took "+str(eras_prime[i][2])+" seconds\n"
    else: line+="\n"
    f.write(line)   #writing one formatted sublist

f.write("Runtime "+str(output_of_eras[1]))

f.close()   #txt saved

check_file_primes(name_of_file)
print("Runtime: "+str(output_of_eras[1])+"s")