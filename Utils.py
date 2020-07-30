import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0

def Screen_cleaner():
    if os.name == "nt":
        os.system('cls')
    else : 
        os.system('clear')
