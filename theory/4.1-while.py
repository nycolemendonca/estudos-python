# Determine a soma dos n primeiros números

amountOfNumbers = 15
sum = 0
count = 0

while count <= amountOfNumbers:
    sum = sum + count
    count = count + 1

print('The sum of first ', amountOfNumbers,' is ', sum)
