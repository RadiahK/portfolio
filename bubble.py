import csv
import string

# Open the CSV File and read it in.
f = open('cities.csv')
data = f.read()

# Split the data into an array of cities.
cities = data.split('\n')

length = len(cities)
#print(cities[1])
#print(cities)



def bubbleSort(cities):
    for passnum in range(len(cities)-1,0,-1):
        for i in range(passnum):
            if cities[i]>cities[i+1]:
                temp = cities[i]
                cities[i] = cities[i+1]
                cities[i+1] = temp

bubbleSort(cities)
print(cities)
