import csv
  
  
filename ="weather.csv"
  
# opening the file using "with" 
# statement
with open(filename, 'r') as data:
      
    for line in csv.DictReader(data):
        for l in line.values():
            lo = l(filter(lambda x:x!=500, dict.items()))
            print(lo)