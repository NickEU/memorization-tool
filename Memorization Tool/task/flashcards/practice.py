from util import loop_input_until_valid_answer


def practice_flashcards(flashcards):
    if not flashcards:
        print('There is no flashcard to practice!')
    else:
        for (question, answer) in flashcards.items():
            start_message = f'Question: {question}\nPlease press "y" to see the answer or press "n" to skip:\n'
            user_input = loop_input_until_valid_answer(start_message, ('y', 'n'))

            if user_input == 'y':
                print(f"Answer: {answer}")
            elif user_input == 'n':
                continue
