import csv
import json

f = open('D:\\Personal\\Freelancer\\UpWork\\Test.csv','rU')
reader=csv.DictReader(f)
out=json.dumps([row for row in reader])
print('JSON parsed')
f=open('D:\\Personal\\Freelancer\\UpWork\\parsed.json','w')
f.write(out)
print('JSON Saved!')