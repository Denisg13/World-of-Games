import random

def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    flag = True
    while flag:
        user_choice = input("Your choice (1-{0}): ".format(difficulty))
        
        if user_choice.isdecimal():
            if 1 <= int(user_choice) <= difficulty:
                return int(user_choice)

def compare_results(sercret_number, user_choice):
    if sercret_number == user_choice:
        return True
    else:
        return False

def play(difficulty):
    sercret_number = generate_number(difficulty)
    user_choice = get_guess_from_user(difficulty)
    return compare_results(sercret_number, user_choice)