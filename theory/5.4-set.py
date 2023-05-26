setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print('A: ', setA)
print('B: ', setB)

print('A union B: ', setA | setB)           # Union
print('A intersection B: ', setA & setB)    # Intersection
print('A difference B: ', setA - setB)      # Difference

setA.add(6)                     # Add element
setA.update([7, 8, 9])          # Add a set of elements
setA.discard(9)                 # Delete element
print(setA.isdisjoint(setB))    # Check elements in common
print(setA.issubset(setB))      # Check if it is subset
print(setA.issuperset(setB))    # Check if it contains another set