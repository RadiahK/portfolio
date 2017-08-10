import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries[1])
print(countries)


def BinarySearch(first, last):
  minx = 0
  maxx = len(countries)
  avg = (minx+maxx)/2
  country=input("Pick a country: " )
  if country == countries[avg]:
      print("Found it at " + avg + " in list. ")
  elif (country < countries[avg]):
      return BinarySearch(first, avg-1)
  elif(country > countries[avg]):
      return BinarySearch(avg + 1, last)
  else:
      print("Oops did not find it")
