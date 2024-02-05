# -------------------- import of libraries -------------------- #
import time
from check_primes import check_file_primes
import os

# -------------------- import of created sieves -------------------- #

from erastosthenes import sieve_of_erastosthenes
from sundaram import sieve_of_sundaram
from atkin import sieve_of_atkin


# -------------------- Input -------------------- #

primes_smaller_max = int(input("Check primes below n, n="))
if primes_smaller_max > 100000000:
    print("Error: Control Script maximum reached!")
    quit()
print()

starttime = time.time()


# -------------------- Create new Working Directory -------------------- #

timenow = time.ctime(time.time()).split()
formattime = (str(timenow[2])+"."+str(timenow[1])+"."+str(timenow[4])+"_"+str(timenow[3]).replace(":","-"))

dir_name = os.path.join(formattime+"_"+str(primes_smaller_max))
parent_dir = "D:/Facharbeit Datensammlung/"

path = os.path.join(parent_dir, dir_name)
os.mkdir(path)
print("Directory "+dir_name+" was successfully created!")
print()


# -------------------- Sieve of Erastosthenes -------------------- #

name_of_eras_file = os.path.join(path, str("Erastothenes_"+formattime)+".txt")
eras_file = open(name_of_eras_file, "w")    #create new file with starttime (before calculating)

output_of_eras = sieve_of_erastosthenes(primes_smaller_max)    #calculating with sieve of Erastosthenes
eras_prime = output_of_eras[0]

# formatting and writing to txt
for i in range(len(eras_prime)):    #for sublists in main list
    line = "Num "+str(eras_prime[i][0])+" is prime: "+str(eras_prime[i][1])
    if type(eras_prime[i][2])!=type(0):                     #if a prime number was found and sieved
        line+=", Operation took "+str(eras_prime[i][2])+" seconds\n"
    else: line+="\n"
    eras_file.write(line)   #writing one formatted sublist

eras_file.write("Runtime "+str(output_of_eras[1])+"\n")  #saving runtime of Sieve of Erastosthenes
eras_file.write(str(output_of_eras[2])+" Checks performed") #saving amount of checks in Sieve of Erastosthenes
eras_file.close()   #txt saved

print("Sieve of Erastosthenes:")
check_file_primes(name_of_eras_file)
print("Runtime: "+str(output_of_eras[1])+"s")
print("Performed Checks: "+str(output_of_eras[2]))
print()

# clean up
output_of_eras = []
eras_prime = []


# -------------------- Sieve of Sundaram -------------------- #

name_of_sund_file = os.path.join(path, str("Sundaram_"+formattime)+".txt")
sund_file = open(name_of_sund_file, "w")    #create new file with starttime (before calculating)

output_of_sund = sieve_of_sundaram(primes_smaller_max)    #calculating with Sieve of Sundaram
sund_prime = output_of_sund[0]

# formatting and writing to txt
for i in range(len(sund_prime)):    #for sublists in main list
    line = "Num "+str(sund_prime[i][0])+" is prime: "+str(sund_prime[i][1])
    if type(sund_prime[i][2])!=type(0):                     #if a prime number was found and sieved
        line+=", Operation took "+str(sund_prime[i][2])+" seconds\n"
    else: line+="\n"
    sund_file.write(line)   #writing one formatted sublist

sund_file.write("Runtime "+str(output_of_sund[1])+"\n")  #saving runtime of Sieve of Sundaram
sund_file.write(str(output_of_sund[2])+" Checks performed") #saving amount of checks in Sieve of Sundaram
sund_file.close()   #txt saved

print("Sieve of Sundaram:")
check_file_primes(name_of_sund_file)
print("Runtime: "+str(output_of_sund[1])+"s")
print("Performed Checks: "+str(output_of_sund[2]))
print()

# clean up
output_of_sund = []
sund_prime = []


# -------------------- Sieve of Atkin -------------------- #

name_of_atki_file = os.path.join(path, str("Atkin_"+formattime)+".txt")
atki_file = open(name_of_atki_file, "w")    #create new file with starttime (before calculating)

output_of_atki = sieve_of_atkin(primes_smaller_max)    #calculating with Sieve of Atkin
atki_prime = output_of_atki[0]

# formatting and writing to txt
for i in range(len(atki_prime)):    #for sublists in main list
    line = "Num "+str(atki_prime[i][0])+" is prime: "+str(atki_prime[i][1])
    if type(atki_prime[i][2])!=type(0):                     #if a prime number was found and sieved
        line+=", Operation took "+str(atki_prime[i][2])+" seconds\n"
    else: line+="\n"
    atki_file.write(line)   #writing one formatted sublist

atki_file.write("Runtime "+str(output_of_atki[1])+"\n")  #saving runtime of Sieve of Atkin
atki_file.write(str(output_of_atki[2])+" Checks performed") #saving amount of checks in Sieve of Atkin
atki_file.close()   #txt saved

print("Sieve of Atkin:")
check_file_primes(name_of_atki_file)
print("Runtime: "+str(output_of_atki[1])+"s")
print("Performed Checks: "+str(output_of_atki[2]))
print()

# clean up
output_of_atki = []
atki_prime = []


# -------------------- End -------------------- #

print("All operations took: "+str(time.time()-starttime))