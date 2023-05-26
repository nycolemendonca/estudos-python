listA = [1, 2, 3, 4, 5]
listB = [3, 1, 5, 9, 0, 8, 2, 3, 4]
listC = [12, 43, 23, 12, 789]

def sumList(list):
        sum = 0
        for item in list: sum += item
        return sum;

sumListA = sumList(listA)
sumListB = sumList(listB)
sumListC = sumList(listC)

print('Sum ListA = ', sumListA)
print('Sum ListB = ', sumListB)
print('Sum ListC = ', sumListC)