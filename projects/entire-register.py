# Entire Register

name = str(input('Name: '))
age = int(input('Age: '))
gender = str(input('Gender (M|F): '))

if gender == 'F' and age >= 62:
    contributionYears = int(input('Contribution years: '))
    if contributionYears >= 15: print('You are eligible to retire!')
    else:
        print('You are not eligible to retire')

elif gender == 'M' and age >= 65:
    contributionYears = int(input('Contribution years: '))
    if contributionYears >= 15: print('You are eligible to retire!')
    else:
        print('You are not eligible to retire')

else:
    print('You are not eligible to retire')
