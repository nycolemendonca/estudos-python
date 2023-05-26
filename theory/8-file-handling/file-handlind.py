import biggestCities.txt as cities

file = open('cities', 'r')

# read(): Read all lines of teh file, and stores the content in a string
content = file.read()

# readlines(): Returns a list of strings, where each element corresponds to a line in the file
# lines = file.readlines()

print(content)
file.close()