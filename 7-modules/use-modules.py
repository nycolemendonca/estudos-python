import areas # Module produced by me
import math # Math functions
import itertools # Construction of elaborate sequences
from datetime import datetime, timedelta # Timestamp handling
import random # Creation of random numbers and sequences
import os # Features that depend on the OS

print(areas.circle(10))
print(areas.square(5))

print('Function Cos: ', math.cos(100))
print('Function Log: ', math.log(8))

print(list(itertools.combinations('ABCD', 3))) # 3 in 3 combo
print(list(itertools.permutations(['A', 'B', 'C'], 2))) # 2 in 2 permutation

print('Current Datetime: ', datetime.now())
print('Datetime after 7 days: ', datetime.now() + timedelta(days=7))

print('Random number between 0 and 1: ', random.random())
print('Random integer between 50 and 100: ', random.randint(50, 100))

os.mkdir('directory') # Create a folder called directory
print('Complete path: ', os.path.join('home/nycol', 'pasta', 'archive.txt'))