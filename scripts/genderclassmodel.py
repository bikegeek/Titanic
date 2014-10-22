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

#Modify data in the fare column to 39 if actual fare is equal to or greater than the fare ceiling:
data[data[0::,9].astype(np.float) >= fareCeiling,9] = fareCeiling - 1.0

fareBracketSize = 10
numFareBrackets = fareCeiling / fareBracketSize


