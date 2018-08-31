
#!/usr/bin/python

# Date Created - 08/28/2019
# Author -Tarun Yadav
# This files contains the code for calculating the average error between predicted and actual of matching stocks within a time window 

#importing csv library to easily read and write to files
import csv

# This function takes the actual and predicted lists and returns a list of errors for matching records. 
def error(actualList,predictedList):
  errors=[]
  for x1 in predictedList:
    for x2 in actualList:
      if (x1[0]==x2[0] and x1[1]==x2[1]):
        #Error contains the time window and the absolute error between the stock and time window match
        errors.append((x1[0],round(abs(float(x1[2])-float(x2[2])),2)))
  return errors

# This function takes alist of sums of errors for a particular time window, the total window length and starting time to start iterating over
def writefile(my_sums,window,start):
  count=0
  total=0
  length=0
  final=[]
  #print(my_sums)
  while count<int(window):
    total +=my_sums[start+count-1][1]
    length +=my_sums[start+count-1][2]
    count += 1

  final.append((start,(start+count-1),round((total/length),2)))

  with open('./output/comparison.txt','a') as f:
    writer = csv.writer(f, delimiter ='|')
    writer.writerows(final)

  print(str(start)+"|"+str(int(start+count-1))+"|"+str(round((total/length),2)))

# Main function to read the files, calls functions to get absolute errors, calculates the sum of all errors for a particular time window and finally call the write file function to write rows to the comparison.txt
def test():

  # open a brand new comparison file  
  comparisonFile=open("./output/comparison.txt","w")

  # open the actual file conatining the readings of actual stocks  
  actualFile=open("./input/actual.txt","r")
  actualReader=csv.reader(actualFile,delimiter="|")

  # convert the list to a list of tuples  
  actualList=[tuple(l) for l in list(actualReader)]
  actualFile.close()

  # open the predictions file
  predictedFile=open("./input/predicted.txt","r")
  predictedReader=csv.reader(predictedFile,delimiter="|")

  # store predictions as kist of tuples
  predictedList=[tuple(l) for l in list(predictedReader)]
  predictedFile.close()

  # get the rolling window
  windowFile=open("./input/window.txt","r")
  window=windowFile.read()
  windowFile.close()
  
  # calculate the max value of the time window
  maxTime=predictedList[len(predictedList)-1][0]

  # calculate the min value of the time window
  minTime=predictedList[0][0]

# get all the absolute errors   
  errors=error(actualList,predictedList)

  # calculate the number of rows that needs to be created in comparison file
  numLoops=(int(maxTime)-int(window))+1
  
  # get the starting position to start calculating the average errors from
  start=int(minTime)

  # store unique time windows in a set
  my_set = {x[0] for x in errors}

  # store all the time windows in a list
  my_list=[x[0] for x in errors]

  #get the sum of errors and total acount  for a particlaur time window
  my_sums = sorted([(i,sum(x[1] for x in errors if x[0] == i),my_list.count(i)) for i in my_set])

  # call the function to write values to the output file
  while start<=numLoops: 
    writefile(my_sums,window,start)
    start += 1
  
  comparisonFile.close()

# Execution of the main program
test()
