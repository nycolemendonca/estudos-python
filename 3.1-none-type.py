names = ['Margot', 'Fred', 'Beyonce']

# Sort method -> Sort the array in ascending order
names = names.sort()
#names.sort() -> correct form

a, b, c = names # non-iterable object
# print(a, b, c) -> correct form
print(names)
# TypeError: Cannot unpack non-iterable NoneType object