questions = ("What is the chemical symbol for gold?",
             "What planet is known as the Red Planet?",
             "Which element is most abundant in the Earth's atmosphere? ",
             "What is the powerhouse of the cell?",
             "What is the largest organ in the human body?")

options = (("A.Au ", "B.Ag ", "C.Pb ", "D.Fe "),
           ("A.Venus ", "B.Mars ", "C.Jupiter ", "D.Saturn "),
           ("A.Oxygen ", "B.Nitrogen ", "C.Carbon Dioxide ", "D.Hydrogen "),
           ("A.Nucleus ", "B.Mitochondria ", "C.Endoplasmic Reticulum ", "D.Ribosome "),
           ("A.Skin ", "B.Heart ", "C.Lung ", "D.Brain "))

answers = ("A", "B", "B", "B", "A")
guesses = []
question_num = 0
score = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct one")
    question_num += 1

print("----------------------")
print("         RESULT       ")   
print("----------------------")

print(" answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


print(" guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

scores = int(score / len(questions) * 100)
print("Your score is: ", scores, "%")


