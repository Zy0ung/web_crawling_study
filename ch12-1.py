import csv
from itertools import count

f = open('./covid19_articles.csv','r')

rd = csv.reader(f)

next(rd)
count = 0

for row in rd:
    if '[속보]' in row[2]:
        print(row[2])
        count += 1

print(f'속보기사 {count}건')
f.close()