import mysql.connector
import csv
import numpy


#Open the train.csv file and import the data into a mySQL database
#

def main():
   #...Open the file
   filename = "/Users/minnawin/Titanic/train1.csv"
   try:
      with open (filename) as f:
         csvData = csv.reader(f)
         #..Build a data structure to store the CSV
         parsedData = []
         fields = csvData.next()
         for row in csvData:
            parsedData.append(row)
         parsedData = numpy.array(parsedData)
         numPassengers = numpy.size(parsedData[0::,1].astype(numpy.float))
         numSurvivors = numpy.sum(parsedData[0::,1].astype(numpy.float))
         proportionSurvivors = (numSurvivors / numPassengers) * 100.

         print "proportion survivors: %2.2f percent" % proportionSurvivors

         womenOnly = parsedData[0::,4] == "female"
         menOnly = parsedData[0::,4] != "female"
         womenOnBoard = parsedData[womenOnly,1].astype(numpy.float)
         menOnBoard = parsedData[menOnly,1].astype(numpy.float)
         proportionWomenSurvivors = (numpy.sum(womenOnBoard) / numpy.size(womenOnBoard))* 100.
         proportionMenSurvivors = (numpy.sum(menOnBoard) / numpy.size(menOnBoard))*100.

         print "Proportion of females who survived: %2.2f percent" % proportionWomenSurvivors
         print "Proportion of males who survived: %2.2f percent" % proportionMenSurvivors

         
   except csv.Error as e:
      print "Error reading CSV file at line %s: %s " % (reader.line_num, e)
      sys.exit(-1)
    

if __name__ == "__main__":
   main()
