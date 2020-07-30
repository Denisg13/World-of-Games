from random import *
import os
import time

def generate_sequence(difficulty):
    numbers_list = []

    for x in range(difficulty):
        numbers_list.append(randint(1, 101))

    return numbers_list
    

def get_list_from_user(difficulty):
    user_numbers_list = []
    for x in range(difficulty):
        user_numbers_list.append(int(input("Please input number from 1 to {0}: ".format(difficulty))))
    return user_numbers_list


def is_lists_equals(numbers_list, user_numbers_list):
    if numbers_list == user_numbers_list:
        return True
    else:
        return False

def play(difficulty):
    num_list = generate_sequence(difficulty)
    print(num_list)
    time.sleep(0.7)
    os.system('cls')
    user_num_list = get_list_from_user(difficulty)
    game_result = is_lists_equals(num_list, user_num_list)
    return game_result
