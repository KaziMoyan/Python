import csv
file = open('example.csv')
file_reader = csv.reader(file)
data = list(file_reader)
print(data)
