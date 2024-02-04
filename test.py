import time
import os

timenow = time.ctime(time.time()).split()
formattime = (str(timenow[2])+"."+str(timenow[1])+"."+str(timenow[4])+"_"+str(timenow[3]).replace(":","-"))

parent_dir = "D:/Facharbeit Datensammlung/"
path = os.path.join(parent_dir, formattime)
os.mkdir(path)

completeName = os.path.join(path, formattime+".txt")

f = open(completeName, "w")
f.write("Test")
f.close()