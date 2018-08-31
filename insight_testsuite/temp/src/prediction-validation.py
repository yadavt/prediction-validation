# Date Created - 08/28/2019
# Author -Tarun Yadav
# This files contains the code for calculating the average error between predicted and actual of matching stocks within a time window 

#!/usr/bin/python

#!/usr/bin/python

#!/usr/bin/python

import csv

def error(actualList,predictedList):
  errors=[]
  for x1 in predictedList:
    for x2 in actualList:
      if (x1[0]==x2[0] and x1[1]==x2[1]):
        errors.append((x1[0],round(abs(float(x1[2])-float(x2[2])),2)))
  return errors

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

def test():

  comparisonFile=open("./output/comparison.txt","w")

  actualFile=open("./input/actual.txt","r")
  actualReader=csv.reader(actualFile,delimiter="|")
  actualList=[tuple(l) for l in list(actualReader)]
  actualFile.close()


  predictedFile=open("./input/predicted.txt","r")
  predictedReader=csv.reader(predictedFile,delimiter="|")
  predictedList=[tuple(l) for l in list(predictedReader)]
  predictedFile.close()

  windowFile=open("./input/window.txt","r")
  window=windowFile.read()
  windowFile.close()
  
  maxTime=predictedList[len(predictedList)-1][0]
  minTime=predictedList[0][0]

  numLoops=(int(maxTime)-int(window))+1
  
  start=int(minTime)

  errors=error(actualList,predictedList)

  my_set = {x[0] for x in errors}
  my_list=[x[0] for x in errors]

  my_sums = sorted([(i,sum(x[1] for x in errors if x[0] == i),my_list.count(i)) for i in my_set])

  while start<=numLoops: 
    writefile(my_sums,window,start)
    start += 1
  
  comparisonFile.close()

test()
