#!/usr/bin/env python
import csv
import matplotlib.pyplot as plt

a = "value"

# graph axises
x=[]
y=[]

#getting csv data from an doc
with open('data.csv') as f:  
    data = csv.reader(f)

    for row in data:
        x.append(int(row[0]))
        y.append(int(row[1]))

#plotting graph
plt.plot(x,y, marker='o')
plt.title('Traffic in day of week')

plt.xlabel('Day of week')
plt.ylabel('Traffic')
plt.show()
