# Python Quiz Game

questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Chicken", "B. Crocodile ", "C. Ostrich", "D. Snake"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"), 
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "C", "A", "A", "B")

guesses = []
score = 0
questionNumber = 0

# Print Questions
for question in questions: 
    print('---------------------')
    print(question)

    # Print Options
    for option in options[questionNumber]: print(option)

    guess = input('Enter (A, B, C, D): ').upper()

    # The append() method is used to add elements at the end of a list
    guesses.append(guess)

    if guess == answers[questionNumber]: 
        score += 1
        print('CORRECT!')
    
    else: 
        print('INCORRECT!')
        print(f'{answers[questionNumber]} is the correct answer')

    questionNumber += 1