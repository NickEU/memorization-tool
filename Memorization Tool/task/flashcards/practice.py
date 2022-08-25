from util import loop_input_until_valid_answer, loop_input_until_nonempty_answer
from db import get_all_flashcards, update_flashcard, delete_flashcard, Flashcard
from enums import LeitnerBox


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


def learning_menu(flashcard):
    print(f"Answer: {flashcard.answer}")
    is_correct_message = 'press "y" if your answer is correct:\npress "n" if your answer is wrong:\n'
    user_input = loop_input_until_valid_answer(is_correct_message, ('y', 'n'))

    if user_input == 'y':
        flashcard.leitner_box = LeitnerBox(flashcard.leitner_box.value + 1)
    elif user_input == 'n':
        flashcard.leitner_box = LeitnerBox.DIFFICULT

    update_flashcard(flashcard)


def practice_flashcards():
    flashcards = get_all_flashcards()
    if not flashcards:
        print('There is no flashcard to practice!')
    else:
        flashcards_sorted_by_difficulty = sorted(flashcards, key=lambda card: card.leitner_box.value)
        for flashcard in flashcards_sorted_by_difficulty:
            start_message = f'Question: {flashcard.question}\n' \
                            f'press "y" to see the answer:\npress "n" to skip:\npress "u" to update:\n'
            user_input = loop_input_until_valid_answer(start_message, ('y', 'n', 'u'))

            if user_input == 'y':
                learning_menu(flashcard)
            elif user_input == 'u':
                update_menu(flashcard)
