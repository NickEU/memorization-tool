from util import loop_input_until_valid_answer, loop_input_until_nonempty_answer
from db import get_all_flashcards, update_flashcard, delete_flashcard, Flashcard


def update_menu(flashcard):
    start_message = 'press "d" to delete the flashcard:\npress "e" to edit the flashcard:\n'
    user_input = loop_input_until_valid_answer(start_message, ('e', 'd'))

    if user_input == 'e':
        question_edit = f"current question: {flashcard.question}\nplease write a new question:\n"
        new_question = loop_input_until_nonempty_answer(question_edit)
        flashcard.question = new_question

        answer_edit = f"current answer: {flashcard.answer}\nplease write a new answer:\n"
        new_answer = loop_input_until_nonempty_answer(answer_edit)
        flashcard.answer = new_answer

        update_flashcard(flashcard)
    elif user_input == 'd':
        delete_flashcard(flashcard)


def practice_flashcards():
    flashcards = get_all_flashcards()
    if not flashcards:
        print('There is no flashcard to practice!')
    else:
        for flashcard in flashcards:
            start_message = f'Question: {flashcard.question}\n' \
                            f'press "y" to see the answer:\npress "n" to skip:\npress "u" to update:\n'
            user_input = loop_input_until_valid_answer(start_message, ('y', 'n', 'u'))

            if user_input == 'y':
                print(f"Answer: {flashcard.answer}")
            elif user_input == 'u':
                update_menu(flashcard)
