questions = ("which one come first , Egg or chicken?",
             "which animal lay the largest eggs?",
             "which is heavier, 1 ton of irons or 1 ton of feathers",
             "What animal can live (for a few seconds) without the head?",
             "DO you like this game so far?")

options = (("A.Chicken ", "B.Egg ", "C.Neither", "D.Both of them came out first"),
           ("A.Ostrich ", "B.Whale ", "C.Chicken ", "D.Eagle "),
           ("A.Irons ", "B.Feathers ", "C.Aren't they the same weight? ", "D.Nuh Uh "),
           ("A.What live without the head? ", "B.Chickens ", "C.Cockroaches ", "D.B&C are correct "),
           ("A.Yes ", "B.No ", "C.Nuh uh ", "D.This is not a fun fact "))

answers = ("B", "A", "C", "D", "D")
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

