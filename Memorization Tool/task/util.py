def loop_input_until_valid_answer(start_message, valid_options):
    user_input = None

    while user_input not in valid_options:
        if user_input is not None:
            print(f'{user_input} is not an option')
        user_input = input(start_message)

    return user_input


def loop_input_until_nonempty_answer(message):
    user_input = ""
    while not user_input or not user_input.strip():
        user_input = input(message)
    return user_input
