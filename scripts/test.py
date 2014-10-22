import numpy
import csv

#Open the file
testFile = open('../test.csv','rb')
testFileObj = csv.reader(testFile)

#Skip the header
header = testFileObj.next()

#Open a file to contain output.
predictionFile = open("genderbasedmodel.csv","wb")
predictionFileObj = csv.writer(predictionFile)

#Read in the test file row by row, and based on the sex, write the survival prediction to the new file.
predictionFileObj.writerow(["PassengerId", "Survived"])
for row in testFileObj:   # for each row in test.csv
   if row[3] == 'female':   # True if female
      predictionFileObj.writerow([row[0],'1'])  #predict 1
   else:  
      predictionFileObj.writerow([row[0],'0'])  #predict 0 - this is a male

#Close all open files.
testFile.close()
predictionFile.close()
