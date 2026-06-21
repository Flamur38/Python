
import csv

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line[1], line[3])
