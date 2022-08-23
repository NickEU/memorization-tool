import util
from flashcards.add import add_flashcards
from flashcards.practice import practice_flashcards


def process_input(user_choice):
    match user_choice:
        case '1':
            return add_flashcards
        case '2':
            return practice_flashcards


def main_menu():
    while True:
        user_input = util.loop_input_until_valid_answer("1. Add flashcards\n2. Practice flashcards\n3. Exit\n",
                                                        ('1', '2', '3'))
        if user_input == '3':
            break

        action = process_input(user_input)
        action()
    print('Bye!')


if __name__ == '__main__':
    main_menu()
