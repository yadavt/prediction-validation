# Date Created - 08/28/2019
# Author -Tarun Yadav
# This files contains the code for calculating the average error between predicted and actual of matching stocks within a time window 

import csv

# Read the input files
def read_input():

    actualFile=open("./input/actual.txt","r")
    actualReader=csv.reader(actualFile,delimiter="|")
    actualList=[tuple(l) for l in list(actualReader)]
    actualFile.close()
    print(actualList)

    predictedFile=open("./input/predicted.txt","r")
    predictedReader=csv.reader(predictedFile,delimiter="|")
    predictedList=[tuple(l) for l in list(predictedReader)]
    predictedFile.close()
    print(predictedList)

    windowFile=open("./input/window.txt","r")
    window=windowFile.read()
    windowFile.close()
    print(window)

read_input()

# Match the stocks between actual and predicted 

# Get the average error for the time window

# Write to the output file