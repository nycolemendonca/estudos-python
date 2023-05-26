birthYear = 2000
currentYear = 2023

age = currentYear - birthYear

# Strings are concatenated with strings, not numbers
print('I have ' + str(age) + ' years.')

# Int Type Conversion
print(float(10)) # 10.0
print(bool(-1)) # True
print(bool(0)) # False

# Float Type Conversion
print(int(9.999)) # 9
print(bool(-0.99)) # True
print(str(-0.99)) # -0.99

# Bool Type Conversion
print(int(True)) # 1
print(float(False)) # 0.00
print(str(True)) # True

# String Type Conversion
print(int('-99')) # -99
print(float('0.01')) # 0.11
print(bool('word')) # True
print(bool('')) # False

# None Type
x = None
print(type(x)) # <class 'NoneType'>

# Convert 'NoneType' to String and to Boolean
print(str(None)) # None
print(bool(None)) # False