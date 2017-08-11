import csv
import string

# Open the CSV File and read it in.
f = open('cities.csv')
data = f.read()

# Split the data into an array of countries.
cities = data.split('\n')

print (cities)

def bubbleSort(cities):
    for x in range(len(cities)-1,0,-1):
        for i in range(x):
            if cities[i]>cities[i+1]:
                temp = cities[i]
                cities[i] = cities[i+1]
                cities[i+1] = temp
bubbleSort(cities)
print(cities)

def sortcities():
    global cities
    cities.sort()

def binarySearch():
    global cities, found, citiesearch, lower_bound, middle_pos, upper_bound

    citiesearch = input("What city are you looking for?")
    lower_bound = 0
    upper_bound = len(cities)-1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound+upper_bound) // 2
        if cities[middle_pos] < citiesearch:
            lower_bound = middle_pos + 1
        elif cities[middle_pos] > citiesearch:
            upper_bound = middle_pos - 1
        else:
            found = True
    if found:
        print("The city is at position", middle_pos)
    else:
        print("The city was not in the list.")

def main():
        sortcities()
        binarySearch()


if __name__ == "__main__":
    main()
