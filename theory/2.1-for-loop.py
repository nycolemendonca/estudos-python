
limit = 10 # Set the limit. The exact limit value is not considered.
 

minors = [] # Array of numbers less than limit
bigger = [] # Array of numbers greather than the limit

# Range Function -> Provides a sequence os integers based upon the function's arguments. 
# The argument can take a single value or a set of values
for i in range(20):

    # Append -> The append method appends an element to the end of the list.
    if (i < limit): minors.append(i)
    elif (i > limit): bigger.append(i)

print('Final Result: ')
print('Minors: ', minors)
print('Bigger: ', bigger)
