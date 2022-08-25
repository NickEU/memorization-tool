from util import loop_input_until_nonempty_answer, loop_input_until_valid_answer
from db import create_flashcard


def add_flashcards():
    while True:
        start_message = "1. Add a new flashcard\n2. Exit\n"
        user_input = loop_input_until_valid_answer(start_message, ('1', '2'))

        if user_input == '2':
            break

        question = loop_input_until_nonempty_answer('Question:')
        answer = loop_input_until_nonempty_answer('Answer:')
        create_flashcard(question, answer)
