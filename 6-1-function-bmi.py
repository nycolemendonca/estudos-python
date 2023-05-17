# Declaration 

def bmi(height, weight):
    bmi = round((weight / (height * height)), 2)
    return bmi


height = float(input('Height: '))
weight = float(input('Weight: '))
print('BMI = ', bmi(height, weight))