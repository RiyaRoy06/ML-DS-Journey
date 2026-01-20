# Goal: Read a csv file into a dictionary.

import csv
with open('data.csv','w',newline='') as f:
  writer=csv.writer(f)
  writer.writerow(["a","b","15"])
with open('data.csv', 'r') as f:
    for r in csv.DictReader(f, fieldnames=['Name', 'House','Age']):
        print(r)
