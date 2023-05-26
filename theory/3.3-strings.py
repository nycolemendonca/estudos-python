word = 'Fox'

# Positive Index
print('First Character: ', word[0])
print('Second Character: ', word[1])
print('Third Character: ', word[2])

# Negative Index
print('Last Charactrer', word[-1])
print('Penultimate Charactrer', word[-2])
print('Antepenultimate Charactrer', word[-3])

# Acessing a character set
word2 = 'library'
print(word2[:3]) # lib
print(word2[2:5]) # bra

# Concatenation and Repetition
w1 = 'Belo'
w2 = 'Horizonte'

print(w1 + ' ' + w2) # Belo Horizonte
print(w1 + ' Monte') # Belo Monte

print(w1 * 3)
print((w1 + ', ') * 3)

# Belonging Operations
w3 = 'Consolação'
w4 = 'sola'

print(w3 in w4)
print(w4 in w3)
print('solar' in w1)
print('solar' not in w2)

# Strings Functions and Methods
w5 = 'Belo Horizonte'
s1 = 'Esta é uma frase, com uma vírgula.'
s2 = '   espaço   '

print(len(w5))
print(w5.upper()) # All uppercase
print(w5.lower()) # All lowercase
print(w5.capitalize()) # First letter Upper

print(w5.replace('Horizonte', 'Monte')) # Belo Monte

print(w5.startswith('Belo'))
print(w5.endswith('Monte'))
print(s1.find('frase')) # Returns the index of the first occurence of the word in the sentence

print(w5.split()) # Turns phrase/string into array
print(s1.split(',')) # Each section separated by a comma becomes an element of the array

print(s2.strip()) # Remove extra spaces at the beginning and end of the string