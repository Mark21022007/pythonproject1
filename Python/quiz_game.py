# quiz_game.py
import random
import colorama

colorama.init()

# Color codes for feedback
CORRECT_COLOR = colorama.Fore.GREEN
INCORRECT_COLOR = colorama.Fore.RED
RESET_COLOR = colorama.Fore.RESET
CATEGORY_COLOR = colorama.Fore.CYAN
SCORE_COLOR = colorama.Fore.MAGENTA
WELCOME_COLOR = colorama.Fore.YELLOW
GAME_OVER_COLOR = colorama.Fore.GREEN
FINAL_SCORE_COLOR = colorama.Fore.BLUE

# Import question modules (replace with your actual module names)
from questions import science, history, math  

CATEGORIES = {
    "science": science,
    "history": history,
    "math": math,
}

def display_welcome_message():
    print(WELCOME_COLOR + "\nWelcome to the Ultimate Quiz Game!\n" + RESET_COLOR)
    print("Answer the questions to the best of your ability.")
    print("Let's begin!\n")

def choose_random_question(category):
    questions = CATEGORIES[category].questions
    return random.choice(questions)

def display_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"]):
        print(f"{i + 1}. {option}")

def get_player_answer(question_data):
    while True:
        try:
            answer = int(input("Your answer (1-{}): ".format(len(question_data["options"]))))
            if 1 <= answer <= len(question_data["options"]):
                return answer
            else:
                print(INCORRECT_COLOR + "Invalid input. Please enter a number within the range." + RESET_COLOR)
        except ValueError:
            print(INCORRECT_COLOR + "Invalid input. Please enter a number." + RESET_COLOR)

def check_answer(player_answer, correct_answer_index):
    return player_answer == correct_answer_index + 1

def display_feedback(is_correct, correct_answer_index, question_data):
    if is_correct:
        print(CORRECT_COLOR + "Correct!" + RESET_COLOR)
    else:
        print(INCORRECT_COLOR + "Incorrect." + RESET_COLOR)
        print("The correct answer was:", question_data["options"][correct_answer_index])

def play_round(score):
    category = random.choice(list(CATEGORIES.keys()))
    question_data = choose_random_question(category)
    correct_answer_index = question_data["options"].index(question_data["correct_answer"])

    print(CATEGORY_COLOR + f"\nCategory: {category.upper()}\n" + RESET_COLOR)
    display_question(question_data)
    player_answer = get_player_answer(question_data)

    if check_answer(player_answer, correct_answer_index):
        display_feedback(True, correct_answer_index, question_data)
        score += 1
    else:
        display_feedback(False, correct_answer_index, question_data)

    return score

def main():
    display_welcome_message()
    score = 0
    num_rounds = 5

    for _ in range(num_rounds):
        score = play_round(score)
        print(SCORE_COLOR + f"Your current score: {score}\n" + RESET_COLOR)

    print(GAME_OVER_COLOR + "\nGame Over!" + RESET_COLOR)
    print(FINAL_SCORE_COLOR + f"Your final score: {score} out of {num_rounds}\n" + RESET_COLOR)

if __name__ == "__main__":
    main()
