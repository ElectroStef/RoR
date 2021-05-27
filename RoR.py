# This script takes in the last 60 data points from a CSV
#The data points are time and pressure. The pressure is converted into
#torr and then graphed aganist time as a line graph. 

#Author: ElectroStef
#Date: 05/26/2021

import csv
import os
import sys
import array
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

time = []
timeArray = []
modifiedTime = []
timeAsFloat = []

pressure = []
presArray = []
modifiedPres = []
presAsFloat = []
convertPres = []

currentDir = os.getcwd()
print("current working dir:", currentDir)

userInput = input("Name of file to be reduced: ")
newFileName = input("Name of new file (i.e RoR of [Compnent Name] WOA-####.csv): ")
plotName = input("Name of Plot (i.e RoR of [Component Name] WOA-####.png): ")
file = currentDir
filePath = os.path.normpath(os.path.join(file, userInput))
newFilePath = os.path.normpath(os.path.join(file, newFileName))
openFile = open(filePath, 'r')
reader = csv.reader(openFile, delimiter = ",")
time = next(reader)
for col in reader:
    pressure.append(col[1])
    time.append(col[0])
openFile.close()

totalLength = (len(pressure)- 1)
sixtyLess = (totalLength - 60)

timeArray = time[sixtyLess:totalLength]
presArray = pressure[sixtyLess:totalLength]

print("this is the length of the modified time array: ", len(timeArray))
print("this is the length of the modified pressure array: ", len(presArray))
#print(presArray)
#print(timeArray)

modifiedPres = np.array(presArray) #pressure in npArray - formatting
modifiedTime = np.array(timeArray) #time in npArray - formatting
#timeAsFloat = modifiedTime.astype(float)

presAsFloat = modifiedPres.astype(float) #string to int
convertPres = 10 ** presAsFloat #convert to torr

print(modifiedTime)
#print(timeAsFloat)
print(convertPres)

xAxis = np.arange(0,60)
yAxis = convertPres

plt.title(plotName)
plt.xlabel('Time in Min')
plt.ylabel('Pressure')
plt.plot(xAxis,yAxis, color = 'red')
plt.show()
plt.savefig(plotName)

#save simplified Raw data
openNewFile = open(newFilePath, 'w+')
writer = csv.writer(openNewFile)
for w in range(60):
    writer.writerow([modifiedTime[w],convertPres[w]])
openNewFile.close()
