#series of question
questions = ("5 + 3 = ?",
             "21 - 17 = ?",
             "11 * 11 = ? ",
             "144 / 12 = ? ",
             "(135 + 65 - 100) / 2 = ?")
#series of options
options = (("A.8 ", "B.9 ", "C.10 ", "D.11 "),
           ("A.3 ", "B.4 ", "C.5 ", "D.6 "),
           ("A.122 ", "B.121 ", "C.133 ", "D.144 "),
           ("A.11 ", "B.10 ", "C.12 ", "D.14 "),
           ("A.12 ", "B.8 ", "C.9 ", "D.10 "))


answers = ("A", "B", "B", "C", "D")
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
print(f"Your score is: ", scores, "%")

