from util import loop_input_until_valid_answer
from db import get_all_flashcards


def practice_flashcards():
    flashcards = get_all_flashcards()
    if not flashcards:
        print('There is no flashcard to practice!')
    else:
        for flashcard in flashcards:
            start_message = f'Question: {flashcard.question}\nPlease press "y" to see the answer or press "n" to skip:\n'
            user_input = loop_input_until_valid_answer(start_message, ('y', 'n'))

            if user_input == 'y':
                print(f"Answer: {flashcard.answer}")
            elif user_input == 'n':
                continue
