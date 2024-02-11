# -------------------- import of libraries -------------------- #
import time
from check_primes import check_file_primes
import os

# -------------------- import of created sieves -------------------- #

from eratosthenes import sieve_of_eratosthenes
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


# -------------------- Sieve of eratosthenes -------------------- #

name_of_erat_file = os.path.join(path, str("Eratosthenes_"+formattime)+".txt")
erat_file = open(name_of_erat_file, "w")    #create new file with starttime (before calculating)

output_of_erat = sieve_of_eratosthenes(primes_smaller_max)    #calculating with sieve of eratosthenes
erat_prime = output_of_erat[0]

# formatting and writing to txt
for i in range(len(erat_prime)):    #for sublists in main list
    line = str(erat_prime[i][0])+" "+str(erat_prime[i][1])
    if type(erat_prime[i][2])!=type(0):                     #if a prime number was found and sieved
        line+=" "+str(erat_prime[i][2])+"\n"
    else: line+="\n"
    erat_file.write(line)   #writing one formatted sublist

erat_file.write("Runtime "+str(output_of_erat[1])+"\n")  #saving runtime of Sieve of eratosthenes
erat_file.write(str(output_of_erat[2])+" Checks performed") #saving amount of checks in Sieve of eratosthenes
erat_file.close()   #txt saved

print("Sieve of eratosthenes:")
check_file_primes(name_of_erat_file)
print("Runtime: "+str(output_of_erat[1])+"s")
print("Performed Checks: "+str(output_of_erat[2]))
print()

# clean up
output_of_erat = []
erat_prime = []


# -------------------- Sieve of Sundaram -------------------- #

name_of_sund_file = os.path.join(path, str("Sundaram_"+formattime)+".txt")
sund_file = open(name_of_sund_file, "w")    #create new file with starttime (before calculating)

output_of_sund = sieve_of_sundaram(primes_smaller_max)    #calculating with Sieve of Sundaram
sund_prime = output_of_sund[0]

# formatting and writing to txt
for i in range(len(sund_prime)):    #for sublists in main list
    line = str(sund_prime[i][0])+" "+str(sund_prime[i][1])
    if type(sund_prime[i][2])!=type(0):                     #if a prime number was found and sieved
        line+=" "+str(sund_prime[i][2])+"\n"
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
    line = str(atki_prime[i][0])+" "+str(atki_prime[i][1])
    if type(atki_prime[i][2])!=type(0):                     #if a prime number was found and sieved
        line+=" "+str(atki_prime[i][2])+"\n"
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