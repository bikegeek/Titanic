import mysql.connector
import csv
import numpy


def createDBTable(parsedData):
       count = 0
       primaryKey =""
       #mySQLString = '"CREATE TABLE IF NOT EXISTS '+ "'passenger'(" + '"'+  "\n"
       mySQLString = '"CREATE TABLE '+ "'passenger'(" + '"'+  "\n"

       # ..First, create the table if it doesn't already exist.
       for data in parsedData:
           if count == 0: 
              count += 1
              for key,value in data.iteritems():
      #           print "key: %s " % key
                 # ..Create the string that creates the mySQL table
                 if key == 'Fare':
                     mySQLString +='"' + "'" + key  + "'" + " DECIMAL(4,4) ," + '"' +"\n"  
                 if key == 'Name':
                     mySQLString += '"' + "'" + key  + "'" + " VARCHAR(80) ," + '"' + "\n"  
                 if key == 'Embarked':
                     mySQLString += '"' + "'" + key + "'"  + " VARCHAR(1) ," + '"' + "\n"  
                 if key == 'Age':
                     mySQLString += '"' + "'" + key + "'"  + " DECIMAL(3,1) ," + '"' + "\n"  
                 if key == 'Parch':
                     mySQLString += '"' + "'" + key + "'"  + " TINYINT(2) ," + '"' + "\n"  
                 if key == 'Pclass':
                     mySQLString += '"' + "'" + key + "'"  + " TINYINT(1) ," + '"' + "\n"  
                 if key == 'Sex':
                     mySQLString += '"' + "'" + key + "'"  + " VARCHAR(1) ," + '"' + "\n"  
                 if key == 'Survived':
                     mySQLString += '"' + "'" + key + "'"  + " VARCHAR(1) ," + '"' + "\n"  
                 if key == 'SibSp':
                     mySQLString += '"' + "'" + key + "'"  + " TINYINT(2) ," + '"' + "\n"  
                 if key == 'PassengerId':
                     primaryKey += key
                     mySQLString += '"' + "'" + key + "'"  + " SMALLINT(4) NOT NULL," + '"' + "\n"  
                 if key == 'Ticket':
                     mySQLString += '"' + "'" + key + "'"  + " VARCHAR(5) ," + '"' + "\n"  
                 if key == 'Cabin':
                     mySQLString += '"' + "'" + key + "'"  + " VARCHAR(80) ," + '"' + "\n"  
                 #print "currently: %s" % mySQLString
           else:
               return mySQLString
           #mySQLString +=  '" PRIMARY KEY ( ' + "'%s') )" + "\n" + ' ENGINE=MYISAM"' % primaryKey
           mySQLString +=  '" PRIMARY KEY ( ' + "'" + primaryKey+ "'" +' )"' + "\n" + '")' +  ' ENGINE=MYISAM"'

       #print "returning mySQLString:\n %s" % mySQLString 
       return mySQLString
#

def popDB(parsedData):
    passwd = 'My$QL4.Minna'
    createTableString =  createDBTable(parsedData)
#123456789012345678901234567890
    dbName = 'titanic'
    connectString = "user = 'root', password = '" + passwd + "', host = 'localhost'"
    conn = mysql.connector.connect(user='root', password='my$QL4.Minna' )
    cursor = conn.cursor()
    try:
       print "create table string: %s" % createTableString
       cursor.execute(createTableString)
    except mysql.connector.Error as err:
       print("Failed creating database table: {}".format(err))
       exit(1)
       
    try:
       conn.database = dbName
    except mysql.connector.Error as err:
       if err.errno == errorcode.ER_BAD_DB_ERROR:
           create_database(cursor)
           conn.database = dbName
       else:
           print(err)
           exit(1)



#Open the train.csv file and import the data into a mySQL database
#

def parseToDictionary():
   #...Open the file
   filename = "/Users/minnawin/Titanic/train1.csv"
   try:
      with open (filename) as f:
         csvData = csv.reader(f)
         #..Build a data structure to store the CSV
         parsedData = []
         fields = csvData.next()
         for row in csvData:
            parsedData.append(dict(zip(fields,row)))
   except csv.Error as e:
      print "Error reading CSV file at line %s: %s " % (reader.line_num, e)
      sys.exit(-1)
    
   return parsedData   



print parseToDictionary()

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
         print parsedData[-1]
   except csv.Error as e:
      print "Error reading CSV file at line %s: %s " % (reader.line_num, e)
      sys.exit(-1)
    

if __name__ == "__main__":
   main()
