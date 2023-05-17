# Counting the number of occurrence of a letter in a word

word = 'banana'
count = 0

for letter in word: 
    if letter == 'a': count += 1

print('The word', word, ' has ', count, ' letters "A".')
