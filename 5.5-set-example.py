# Management of a Language School
# 3 Groups of students -> English, French and Spanish
# A student can be enrolled in one or more classes

englishClass = {'Gabriel', 'Caio', 'Maria', 'Ana', 'Juliano', 'Flávia', 'Rubens', 'Bruna'}
spanishClass = {'Caio', 'Arthur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui'}
frenchClass = {'Pedro', 'Bruna', 'Paula', 'Thiago', 'Maria', 'Flavia', 'Rui', 'Carolina'}

allStudents = englishClass | spanishClass | frenchClass
print('All students: ', allStudents)

# Students enrolled in more than one class
moreThanOneClass = (englishClass & spanishClass) | (spanishClass & frenchClass) | (englishClass & frenchClass)
print(moreThanOneClass)

