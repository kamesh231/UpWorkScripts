import csv
newrow = []
fileRead = sys.argv[0]
fileWrite = sys.argv[1]
csvFileRead = open('c:/temp/csvfile.csv', 'rb')
csvFileNew = open('c:/temp/csvfilenew.csv', 'wb')

# Open the CSV
csvReader = csv.reader(csvFileRead, delimiter = ',')

# Append the rows to variable newrow
for row in csvReader:
    newrow.append(row)

# Add quotes around the list items
for row in newrow:
    row[0] = "'"+str(row[0])+"'"
	row[1] = "'"+str(row[1])+"'"
    row[2] = "'"+str(row[2])+"'"

csvFileRead.close()

# Create a new CSV file
csvWriter = csv.writer(csvFileNew, delimiter = ',')

# Append the csv with rows from newrow variable
for row in newrow:
    csvWriter.writerow(row)

csvFileNew.close()