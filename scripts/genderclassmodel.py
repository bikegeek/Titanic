import csv
import numpy as np

# Open csv file and read it
csvFileObj = csv.reader(open('../train.csv', 'rb'))

header = csvFileObj.next()

data = []
for row in csvFileObj: # loop through each row in the csv file
   data.append(row)    # copy each row into the list

data = np.array(data)  # convert the list into an array

# Generate bins of ticket prices.
# Create the ceiling for the fare.
fareCeiling = 40

#Modify data in the fare column to 39 if actual fare is equal to or greater than the fare ceiling
#so we have equal sized bins for $0-9, $10-19, $20-29, and $30-39
data[data[0::,9].astype(np.float) >= fareCeiling,9] = fareCeiling - 1.0

fareBracketSize = 10
numberOfFareBrackets = fareCeiling / fareBracketSize

#Hard-code the number of classes on board
numberOfClasses = 3

#Compute the number of classes from the data by searching for the number
#of unique values in column index 2
numberOfClasses = len(np.unique(data[0::,2]))

#Initialize the survival table, set all values to 0.
survivalTable = np.zeros((2,numberOfClasses, numberOfFareBrackets))

#Loop through every variable and match to any passengers that agree with the 
#statements
for i in xrange(numberOfClasses):
   for j in xrange(numberOfFareBrackets):
       womenOnlyStats = data[    
                           (data[0::,4] == "female") 
                        &(data[0::,2].astype(np.float) 
                              == i+1)   
                        &(data[0::,9].astype(np.float)  
                           >= j*fareBracketSize )
                        &(data[0::,9].astype(np.float) 
                             < (j+1)*fareBracketSize),1]
       menOnlyStats = data[          \
                          (data[0::,4] != "female") 
                         &(data[0::,2].astype(np.float) 
                               == i+1)         
                         &(data[0::,9].astype(np.float) 
                               >= j*fareBracketSize)  
                         &(data[0::,9].astype(np.float) 
                               < (j+1)*fareBracketSize),1]
       survivalTable[0,i,j] = np.mean(womenOnlyStats.astype(np.float))
       survivalTable[1,i,j] = np.mean(menOnlyStats.astype(np.float))

       survivalTable[survivalTable != survivalTable ] = 0.
 

print survivalTable
