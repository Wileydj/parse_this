import csv 

sampleDataCsv = open("sample_data.csv") # opening the .csv file

sampleDataReader = csv.reader(sampleDataCsv) #making the variable csvfile into a reader object

next(sampleDataReader) #skip the first line (contains information which is not integers

sortedByInts = sorted(sampleDataReader, key = lambda x: int(x[1])) #sort the data according to the elements in column 2, according to their ascending value


i = 0 #establishing a counter

for i in range(5000): # establishing a range which represents the entire data sheet
	if int(sortedByInts[i][1]) < 1405987200 and int(sortedByInts[i][1]) > 1403395200: #selects only data which exists between the dates June, 22, 2014 and July 22, 2014
		print(sortedByInts[i][8]) #prints any data in the 8th column which is between those timestamps
		i += 1 #increments after printing
	else:
		i += 1 #increments even if we don’t print!