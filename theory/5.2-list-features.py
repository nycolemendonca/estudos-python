list = [2, 'margot', 'b', 3.18, True]

# Add the element at the end of the list
list.append('soraya')

# Replaces the first element of the list and delete the previous
list[0] = 'nycole'

# Removes the first occurrence of the element 'b'
list.remove('b')

# ================================================================

listOne = [30, 10, 20]
listTwo = [2, 'n', 3.16, True]

print(listOne + listTwo)    # Concatenate
print(listOne * 2)          # Repetition
print(10 in listOne)        # Affiliation


print(len(listTwo)) # Size
print(sum(listOne)) # Sum
print(max(listOne)) # Bigger value

listTwo.reverse()                       # Reverses the order of the elements
listOne.extend([10, 20, 30, 40, 10])    # Add elements
listOne.sort()                          # Sort the list values
listTwo.pop()                           # Remove the last element
listTwo.clear()                         # Remove all elements

print(listOne.index(40)) # Returns the index of the first occurrence of the element
print(listOne.count(10)) # Counts the occurrences of the element
