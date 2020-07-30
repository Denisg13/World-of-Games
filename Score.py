from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    try:
        scores_file = open(SCORES_FILE_NAME, 'r')
        current_score = scores_file.read()
        scores_file.close()
        points_of_winning = (int(difficulty) * 3) + 5 + int(current_score)        
    except:
        points_of_winning = (int(difficulty) * 3) + 5
    finally:
        scores_file = open(SCORES_FILE_NAME, 'w')
        scores_file.write(str(points_of_winning))
        scores_file.close()
